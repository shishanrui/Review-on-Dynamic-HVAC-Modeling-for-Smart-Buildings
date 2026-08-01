# Sub-keyword Synonym Subtopics Searching (SSSS)

This directory contains the Python scripts used to perform and process the literature search for the review of dynamic HVAC modeling in smart buildings.

## Attribution

The scripts were adapted from the [SSSS repository developed by Zhang et al.](https://github.com/lz356/SSSS/tree/master). The underlying search method is described in:

> Zhang, L., Wen, J., Li, Y., Chen, J., Ye, Y., Fu, Y., & Livingood, W. (2021). A review of machine learning in building load prediction. *Applied Energy, 285*, 116452. https://doi.org/10.1016/j.apenergy.2021.116452

Project-specific adaptations include the search terms, subtopics, publication-year range, and title-screening workflow used for the present review.

## Files

- `base.py`: generates combinations of sub-keywords and executes the searches.
- `scholar.py`: provides the Google Scholar query and parsing functions; its original copyright and redistribution notice is retained in the source file.
- `run.py`: defines the project-specific search terms and search settings.
- `screen_ssss_titles.py`: supports title screening of the retrieved records.

