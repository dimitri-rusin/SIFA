import gzip
import medpy.io as medio
import numpy as np
import os
import shutil

def extract_gz(source_path, dest_path):
    with gzip.open(source_path, 'rb') as f_in:
        with open(dest_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def nii2npz(data_nii_pth, label_nii_pth, npz_pth):
    data_arr, _ = medio.load(data_nii_pth)
    label_arr, _ = medio.load(label_nii_pth)
    np.savez(npz_pth, data_arr, label_arr)

if __name__=="__main__":
    base_path = 'data/test_ct_image&labels/'
    pairs = ['1003', '1008', '1014', '1019']

    for number in pairs:
        data_gz_path = os.path.join(base_path, 'image_ct_{}.nii.gz'.format(number))
        label_gz_path = os.path.join(base_path, 'gth_ct_{}.nii.gz'.format(number))

        # Extract the gz files
        data_nii_path = data_gz_path.rstrip('.gz')
        label_nii_path = label_gz_path.rstrip('.gz')

        extract_gz(data_gz_path, data_nii_path)
        extract_gz(label_gz_path, label_nii_path)

        # Define the output npz path and remove it if it already exists
        output_path = os.path.join(base_path, '{}.npz'.format(number))
        if os.path.exists(output_path):
            os.remove(output_path)

        # Convert nii to npz
        nii2npz(data_nii_path, label_nii_path, output_path)

        # Remove the intermediate nii files
        os.remove(data_nii_path)
        os.remove(label_nii_path)
