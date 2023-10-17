Dataset **Maize Tassel Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/g/1/Gb/em6ZTet7iOgqgJLWtkGev6YkNqmEDyHnzHgArw1CNHyBR9BsPnbzogPFSh6yylXPxkHHvR9rVBFPQ4kLFkYUbAHMGgO6GqWOVvLg8ThLpW3OphLvUQFWyxRmmgX4.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Maize Tassel Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/4922074/files/Maize_Tassels_Recognition.zip?download=1).