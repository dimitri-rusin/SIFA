# How to get it working

Here's a guide how to evaluate the provided SIFA model, which was trained on MRI images and adapted to the domain of CT images. We test how well the adapted model performs on provided CT images.

Follow along!

## Step 1/4: Download the testing data
Go to [Google Drive](https://drive.google.com/file/d/1SJM3RluT0wbR9ud_kZtZvCY0dR9tGq5V/view) and download the `.zip` archive. This might take 1 minute. Extract the archive into the folder
```sh
data/test_ct_image&labels/
```
This will yield the following 8 files:
```sh
data/test_ct_image&labels/gth_ct_1003.nii.gz
data/test_ct_image&labels/gth_ct_1008.nii.gz
data/test_ct_image&labels/gth_ct_1014.nii.gz
data/test_ct_image&labels/gth_ct_1019.nii.gz
data/test_ct_image&labels/image_ct_1003.nii.gz
data/test_ct_image&labels/image_ct_1008.nii.gz
data/test_ct_image&labels/image_ct_1014.nii.gz
data/test_ct_image&labels/image_ct_1019.nii.gz
```

## Step 2/4: Download the model weights
Also, go to [Dropbox](https://www.dropbox.com/sh/787kmmuhvh3e3yb/AAC4qxBJTWwQ1UMN5psrN96ja?dl=0) and scroll to the bottom. Download the following files:
```sh
sifa-cardiac-mr2ct.data-00000-of-00001
sifa-cardiac-mr2ct.index
sifa-cardiac-mr2ct.meta
```
This might take 2 minutes.

Place these three files into the local directory `SIFA-model`.

## Step 3/4: Build a Docker image.

Run
```sh
./INSTALL
```

This will create a new Docker image in your local Docker installation.

## Step 4/4: Run the Docker image.

Run
```sh
./RUN
```
The command might not stop for about 20 minutes. You might need to be patient. It will write 4 files to `data/test_ct_image&labels`. Eventually, you might get an output like the following:
```sh
Dice:
AA :78.3(3.0)
LAC:77.5(5.3)
LVC:73.1(8.6)
Myo:61.2(7.9)
Mean:72.5
ASSD:
AA :9.3(1.6)
LAC:8.7(3.7)
LVC:7.0(2.4)
Myo:6.9(2.1)
Mean:8.0
```

<br>
<br>

---


## Unsupervised Bidirectional Cross-Modality Adaptation via Deeply Synergistic Image and Feature Alignment for Medical Image Segmentation

Tensorflow implementation of our unsupervised cross-modality domain adaptation framework. <br/>
This is the version of our [TMI paper](https://arxiv.org/abs/2002.02255). <br/>
Please refer to the branch [SIFA-v1](https://github.com/cchen-cc/SIFA/tree/SIFA-v1) for the version of our AAAI paper. <br/>

## Paper
[Unsupervised Bidirectional Cross-Modality Adaptation via Deeply Synergistic Image and Feature Alignment for Medical Image Segmentation](https://arxiv.org/abs/2002.02255)
<br/>
IEEE Transactions on Medical Imaging
<br/>
<br/>
<p align="center">
  <img src="figure/framework.png">
</p>

## Installation
* Install TensorFlow 1.10 and CUDA 9.0
* Clone this repo
```
git clone https://github.com/cchen-cc/SIFA
cd SIFA
```

## Data Preparation
* Raw data needs to be written into `tfrecord` format to be decoded by `./data_loader.py`. The pre-processed data has been released from our work [PnP-AdaNet](https://github.com/carrenD/Medical-Cross-Modality-Domain-Adaptation). The training data can be downloaded [here](https://drive.google.com/file/d/1m9NSHirHx30S8jvN0kB-vkd7LL0oWCq3/view). The testing CT data can be downloaded [here](https://drive.google.com/file/d/1SJM3RluT0wbR9ud_kZtZvCY0dR9tGq5V/view). The testing MR data can be downloaded [here](https://drive.google.com/file/d/1Bm2uU4hQmn5L3GwXz6I0vuCN3YVMEc8S/view?usp=sharing).
* Put `tfrecord` data of two domains into corresponding folders under `./data` accordingly.
* Run `./create_datalist.py` to generate the datalists containing the path of each data.

## Train
* Modify the data statistics in data_loader.py according to the specifc dataset in use. Note that this is a very important step to correctly convert the data range to [-1, 1] for the network inputs and ensure the performance.
* Modify paramter values in `./config_param.json`
* Run `./main.py` to start the training process

## Evaluate
* Our trained models can be downloaded from [Dropbox](https://www.dropbox.com/sh/787kmmuhvh3e3yb/AAC4qxBJTWwQ1UMN5psrN96ja?dl=0).
  Note that the data statistics in evaluate.py need to be changed accordingly as specificed in the script.
* Specify the model path and test file path in `./evaluate.py`
* Run `./evaluate.py` to start the evaluation.

## Citation
If you find the code useful for your research, please cite our paper.
```
@article{chen2020unsupervised,
  title     = {Unsupervised Bidirectional Cross-Modality Adaptation via 
               Deeply Synergistic Image and Feature Alignment for Medical Image Segmentation},
  author    = {Chen, Cheng and Dou, Qi and Chen, Hao and Qin, Jing and Heng, Pheng Ann},
  journal   = {arXiv preprint arXiv:2002.02255},
  year      = {2020}
}

@inproceedings{chen2019synergistic,
  author    = {Chen, Cheng and Dou, Qi and Chen, Hao and Qin, Jing and Heng, Pheng-Ann},
  title     = {Synergistic Image and Feature Adaptation: 
               Towards Cross-Modality Domain Adaptation for Medical Image Segmentation},
  booktitle = {Proceedings of The Thirty-Third Conference on Artificial Intelligence (AAAI)},
  pages     = {865--872},
  year      = {2019},
}
```

## Acknowledgement
Part of the code is revised from the [Tensorflow implementation of CycleGAN](https://github.com/leehomyc/cyclegan-1).

## Note
* The repository is being updated
* Contact: Cheng Chen (chencheng236@gmail.com)
