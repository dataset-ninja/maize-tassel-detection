# Path to the original dataset

import supervisely as sly
import os
import xml.etree.ElementTree as ET
import xmltodict


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project_info = api.project.get_info_by_name(workspace_id, project_name)
    if project_info is not None:
        api.project.remove(project.id)
    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta()

    dataset_path = os.path.expanduser("~\Documents\Maize_Tassels_Recognition")
    img_paths = sly.fs.list_files(os.path.join(dataset_path, "2_Raw_RGB_Images_Collected_by_UAV"))
    dataset = api.dataset.create(project.id, "ds0", change_name_if_conflict=True)
    for path in img_paths:
        # get image path and upload
        ann_path = os.path.join(
            dataset_path,
            "3_Labels_for_CNN",
            "Labels",
            (sly.fs.get_file_name(path) + ".xml"),
        )
        try:
            tree = ET.parse(ann_path)
        except Exception as e:
            print(f"EXCEPTION: {e}")
            noann_image_info = api.image.upload_path(dataset.id, sly.fs.get_file_name(path), path)
            print(f"uploaded image with no annotations: image id:{noann_image_info.id}")
            continue
        xml_data = tree.getroot()
        xmlstr = ET.tostring(xml_data, encoding="utf-8", method="xml")

        data_dict = dict(xmltodict.parse(xmlstr))

        image_info = api.image.upload_path(dataset.id, data_dict["annotation"]["filename"], path)
        labels = []
        if "object" not in data_dict["annotation"]:
            continue
        if type(data_dict["annotation"]["object"]) == list:
            for obj in data_dict["annotation"]["object"]:
                # get bbox cords
                xmin = int(obj["bndbox"]["xmin"])
                ymin = int(obj["bndbox"]["ymin"])
                xmax = int(obj["bndbox"]["xmax"])
                ymax = int(obj["bndbox"]["ymax"])

                # get class name, create labels
                bbox = sly.Rectangle(top=ymin, left=xmin, bottom=ymax, right=xmax)
                class_name = obj["name"]
                obj_class = meta.get_obj_class(class_name)
                if obj_class is None:
                    obj_class = sly.ObjClass(class_name, sly.Rectangle)
                    meta = meta.add_obj_class(obj_class)
                    api.project.update_meta(project.id, meta)
                label = sly.Label(bbox, obj_class)
                labels.append(label)

            # upload annotation
            ann = sly.Annotation(
                img_size=[
                    int(data_dict["annotation"]["size"]["height"]),
                    int(data_dict["annotation"]["size"]["width"]),
                ],
                labels=labels,
            )
            api.annotation.upload_ann(image_info.id, ann)
            print(f"uploaded bbox to image(id:{image_info.id})")
        else:
            xmin = int(data_dict["annotation"]["object"]["bndbox"]["xmin"])
            ymin = int(data_dict["annotation"]["object"]["bndbox"]["ymin"])
            xmax = int(data_dict["annotation"]["object"]["bndbox"]["xmax"])
            ymax = int(data_dict["annotation"]["object"]["bndbox"]["ymax"])
            bbox = sly.Rectangle(top=ymin, left=xmin, bottom=ymax, right=xmax)
            class_name = data_dict["annotation"]["object"]["name"]
            obj_class = meta.get_obj_class(class_name)
            if obj_class is None:
                obj_class = sly.ObjClass(class_name, sly.Rectangle)
                meta = meta.add_obj_class(obj_class)
                api.project.update_meta(project.id, meta)
            label = sly.Label(bbox, obj_class)
            labels.append(label)

            # upload annotation
            ann = sly.Annotation(
                img_size=[
                    int(data_dict["annotation"]["size"]["height"]),
                    int(data_dict["annotation"]["size"]["width"]),
                ],
                labels=labels,
            )
            api.annotation.upload_ann(image_info.id, ann)
            print(f"uploaded bbox to image(id:{image_info.id})")
    print(f"Dataset {dataset.id} has been successfully created.")

    return project_info
