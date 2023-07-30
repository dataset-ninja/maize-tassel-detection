Please visit dataset [homepage](https://zenodo.org/record/4922074#.Yk_rlX9Bzmg) to download the data. 

Afterward, you have the option to download it in the universal supervisely format by utilizing the *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Maize Tassel Detection', dst_path='~/dtools/datasets/Maize Tassel Detection.tar')
```
