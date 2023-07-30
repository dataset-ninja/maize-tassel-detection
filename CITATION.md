If you make use of the Maize Tassel Detection data, please cite the following reference:

```bibtex
@dataset{shi_yeyin_2021_4922074,
  author       = {Shi, Yeyin and
                  Alzadjali, Aziza and
                  Alali, Mohammed and
                  Veeranampalayam-Sivakumar, Arun-Narenthiran and
                  Deogun, Jitender and
                  Scott, Stephen and
                  Schnable, James},
  title        = {{Maize tassel detection from UAV imagery using deep 
                   learning}},
  month        = jun,
  year         = 2021,
  note         = {{<p>There are three folders when you download and 
                   unzip the file here named
                   "Maize\_Tassels\_Recognition.zip":</p>  <ul>
                   <li>1\_ReadMe</li>
                   <li>2\_Raw\_RGB\_Images\_Collected\_by\_UAV</li>
                   <li>3\_Labels\_for\_CNN</li> </ul>  <p>In the
                   1\_ReadMe filder, there is a "readme.txt" file with
                   brief descriptions for the labels in the folder
                   3\_Labels\_for\_CNN:</p>  <p>a) xml files are
                   annotated images used to generate the labels, they
                   are used as an input to xml\_to\_csv.py script which
                   is going to generate a csv file.<br> b) The
                   generated csv file is used as an input to generate
                   the tfrecord files using the generate\_tfrecord.py
                   script as shown in below example:<br> \# Create
                   train data:  python generate\_tfrecord.py
                   --csv\_input='path to csv file'
                   --output\_path='path to output tfrecord file'<br>
                   </p> <p>Funding provided by: University of
                   Nebraska-Lincoln<br>Crossref Funder Registry ID:
                   http://dx.doi.org/10.13039/100008114<br>Award
                   Number: A-0000000325</p><p>Funding provided by:
                   U.S. Department of Agriculture<br>Crossref Funder
                   Registry ID:
                   http://dx.doi.org/10.13039/100000199<br>Award
                   Number: 1011130</p>}},
  publisher    = {Zenodo},
  doi          = {10.5061/dryad.r2280gbcg},
  url          = {https://doi.org/10.5061/dryad.r2280gbcg}
}
```

[🔗 Source](https://zenodo.org/record/4922074/export/hx)
