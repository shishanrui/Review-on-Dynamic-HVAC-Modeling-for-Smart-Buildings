#!/usr/bin/env python
"""
Screen SSSS-harvested papers by title against exclusion criteria
---------------------------------------------------------------
Usage:
    python screen_ssss_titles.py  summary.csv(xlsx)  screened.csv(xlsx)

If you omit the output name it defaults to
    <input stem>_screened.<same extension>
"""

import argparse, re, sys
from pathlib import Path
import pandas as pd

# ------------------------- edit here if you need ---------------------- #
CRITERIA = {
    # E1: Domain outside building-HVAC
    "domain_outside_HVAC": [
        r"reactor", r"distillation", r"combustion", r"engine", r"turbine",
        r"battery", r"fuel cell", r"automotive", r"aerospace", r"aircraft",
        r"marine", r"ship", r"rocket", r"cryogenic",  r"robot", r"vehicle", r"bear", r"bearing",
        r"process\s+intensification", r"hexacopter",
        r"power plant", r"chemistry", r"magnet", r"motor", r"furnace", r"power generation",
        r"electrochemical", r"eddy currents",
        r"growth", r"metabolism", r"desalination", r"oil", r"farm", r"voltage", r"treatment",
        r"bridges", "plasma",

    ],
    # E2: Residential / industrial / data-centre / passive cases
    "residential_or_industrial_or_datacenter": [
        r"residential", r"\bhouse\b", r"dwelling", r"apartment", r"\bflat\b",
        r"single[- ]family", r"industrial", r"factory", r"warehouse",
        r"data[\s-]?center", r"server\s+farm", r"greenhouse",
        r"passive",
    ],
    # E3: Static models only
    "static_model_only": [
        r"steady[- ]state", r"\bstatic model\b", r"design day", r"bin method",
        r"quasi[- ]steady"
    ],
    # E4: Control papers without modelling
    # This flag needs manual check
    "control_only_no_model": [r"\bcontrol\b"],
    # E5: Airflow-only CFD without HVAC equipment
    # This flag needs manual check
    "airflow_CFD_only": [
        r"\bcfd\b", r"computational fluid dynamics", r"natural ventilation",
        r"\bairflow\b", r"air flow"
    ],
    # E6: Design-stage sizing / load calcs
    "design_stage_sizing": [
        r"\bsizing\b", r"load calculation", r"cooling load", r"heating load",
        r"design load", r"design calculation"
    ],
}
EQUIPMENT_WORDS = (
    r"hvac|vav|ahu|air handling unit|chiller|boiler|heat pump|fan coil"
    r"|vrf|vrv|vapor compression|vapour compression"
)


# ---------------------------------------------------------------------- #

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Screen SSSS result by title.")
    p.add_argument("input", help="input CSV or XLSX file from SSSS")
    p.add_argument("output", nargs="?", help="output file (optional)")
    return p.parse_args()


def load_frame(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    sys.exit(f"Unsupported file type: {path.suffix}")


def reasons_for(title_norm: str) -> list[str]:
    reasons: list[str] = []
    for key, patterns in CRITERIA.items():
        if key == "control_only_no_model":
            if (re.search(patterns[0], title_norm)
                    and not re.search(r"model|dynamic|simulation", title_norm)):
                reasons.append(key)
            continue
        if key == "airflow_CFD_only":
            if (re.search("|".join(patterns), title_norm)
                    and not re.search(EQUIPMENT_WORDS, title_norm)):
                reasons.append(key)
            continue
        if re.search("|".join(patterns), title_norm):
            reasons.append(key)
    return reasons


def main() -> None:
    args = parse_args()
    in_path  = Path(args.input).expanduser().resolve()
    out_path = (Path(args.output).expanduser().resolve()
                if args.output else
                in_path.with_stem(in_path.stem + "_screened"))

    df = load_frame(in_path)

    if "title" not in df.columns:
        sys.exit("No 'title' column found in the input file.")

    # normalise titles for robust matching
    df["_title_norm"] = (df["title"].astype(str)
                         .str.lower()
                         .str.replace(r"\s+", " ", regex=True)
                         .str.strip())

    df["exclusion_reasons"] = df["_title_norm"].apply(reasons_for)
    df["exclude"] = df["exclusion_reasons"].apply(bool)
    df = df.drop(columns="_title_norm")

    # save
    if out_path.suffix in {".xlsx", ".xls"}:
        df.to_excel(out_path, index=False)
    else:
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    total = len(df)
    excluded = int(df["exclude"].sum())
    remaining = total - excluded
    print(f"▲ {total} rows processed → {excluded} flagged, {remaining} kept")
    print(f"▶ Written: {out_path}")


if __name__ == "__main__":
    main()
