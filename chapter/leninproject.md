# AWS Sagemaker Ground Truth sp20-516-253, Arivukadal, lenin

### AWS Rekognition Introduction:

Amazon Sagemaker is a managed service that enables data scientist, and developers to develop, build, train and deploy machine learning models quickly with very minimal upfront investment in hardware. Being one of the popular AWS cloud managed service, this completely eliminates heavy lift tasks such as hardware provisioning and scaling to help developers to create high quality models by easily select all popular algorithm.

In general, the Machine learning, development process is complex and quite expensive process as there is no integrated tools for the entire ML workflow. This makes, developer and scientist to research and try many different tools and then stitch it together to create workflows and framework, which is most of the time very time consuming and also error-prone process.
SageMaker solves all of these challenges by providing all the necessary components required for machine learning process in a single toolkit as a service so the production ready models are created faster with minimal effort and cost.

![Building Blocks of Amazon SageMaker](https://d1.awsstatic.com/re19/Sagemaker/SageMaker_Overview-Chart.247eaea6e41ddca8299c5a9a9e91b5d78b751c38.png)


## AWS Sagemaker Groundtruth Introduction:
Before we talk about AWS SageMaker Groundtruth, let us understand the differnce between supervwised and unsupervised mchine learning technique:

## Supervised Learning:
In Supervised learning technique, well "labeled" data will be used to train the model. Here, mechine learning algorithm learns from the existing labeled training data and helps developer to predict outcomes for unforeseen data.

## UnSupervised Learning:
In Unsupervised learning technique, develoepr will allow the model to work on its own to discover information. It mainly deals with the unlabelled data. Because of this, unsupervised learning algorithms allow developers to perform more complex processing tasks compared to supervised learning. 

![Supervised vs Unsupervised](https://learncuriously.files.wordpress.com/2018/12/supervised-learning-diagram.jpg)

## Oky, what is the challange in using unsupervised learning? 
Below are some of the major challages:
1. When exploring data using cluster, it is hard to define the number of cluster groups.
2. Unlike supervised learning; evaluating the metrics and results are very difficult as there is no baseline ground truth (labes) to cross verify.

#### What is Amazon SageMaker GroundTruth?
SageMaker GroundTruth is an AWS Managed service which helps the users to accurately label the given dataset in a very efficient and quicker way. There are many approaches that enterprise use to label the large data sets, like using their own workforce (employees) or one of the third party labeling service providers or using Amazon Mechanical Turk workforce (crowdsourced).
Amazon SageMaker GroundTruth uses the most innovative algorithms to improve the accuracy of human labeling process. Over time, SageMaker GroundTruh model gets improved in a progressive way by learning continuously from the human created labels and further increase speed and efficiency of automatic labeling process.

Under the hood, SageMaker GroundTruth use the machine learning to automate the data labeling process. As a first step, the service selects some random samples from the given data set and send it to humans to get labeled. AAs a next step the results are used to further train the underlying machine learning labeling model which further attempts to label any given new raw datasets automatically. Also, the final lables are committed only when the model gets the confidence score, which meets or exceeds the highest threshold. If the confidence score goes below the threshold, the dataset samples will be sent it to human for re-labeling process to improve the accuracy. This cycle gets repeated with the every given sample raw data to the model becomes more capable to automatically label the raw data with very high accuracy and less intervention to human corrections and further labeling.

AWS Official FAQ:

* <https://aws.amazon.com/sagemaker/groundtruth/faqs/>

#### Amazon SageMaker Ground Truth Features

## 1. Automated Data Labeling
At a high-level, the service uses the required machine learning algorithm to improve the accuracy and reduce the human intervention for review and labeling to automate the overall process. 

## 2. Flexibility in how you work with labeling professionals
The service supports various options for manual labeling directly in the SageMaker Ground Truth Console. For an example; Using private workforce or AWS Mechanical Turk or AWS market place (verified) professionals. 

## 3.Easy instructions for human labeling
GroundTruh service helps the user to follow industry standard and best practice guidance to label any given data set.
For an example: Following visual instruction is one of the example to help user to attain the highest standard to label the objecgt.

![Building Blocks of Amazon SageMaker](https://d1.awsstatic.com/r2018/r/Samurai/SamurAI%20Customer%20Assets/SamurAI%20Instructions%20for%20Bounding%20Box.c942d04c735161bbd6c8979f371fa9f7ef5a9fc3.png)

## 4.Use workflows to simplify labeling tasks
GroundTruth comes with built in workflows such as object detection, text classification, semantic segmentation, image classification that helps human labels to follow step by step instruction to produce high-accuracy.

#### Pricing

User only pay for each labeled object labeled automatically by SageMaker GroundTruth or human labeler. These objects can be  the section of text or an image or an audio recording, etc.,. Or, If an user hire a vendor or AWS Mechanical Turk service to provide labels, they will pay an additional cost per labeled object. 

* <https://aws.amazon.com/sagemaker/groundtruth/pricing/>


