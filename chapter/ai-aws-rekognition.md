# AWS Rekognition sp20-516-253, Arivukadal, Lenin

AWS Sagemaker Introduction:

Amazon Rekognition makes it easy to add image and video analysis to your applications using proven, highly scalable, deep learning technology that requires no machine learning expertise to use. With Amazon Rekognition, you can identify objects, people, text, scenes, and activities in images and videos, as well as detect any inappropriate content. Amazon Rekognition also provides highly accurate facial analysis and facial search capabilities that you can use to detect, analyze, and compare faces for a wide variety of user verification, people counting, and public safety use cases.

With Amazon Rekognition Custom Labels, you can identify the objects and scenes in images that are specific to your business needs. For example, you can build a model to classify specific machine parts on your assembly line or to detect unhealthy plants. Amazon Rekognition Custom Labels takes care of the heavy lifting of model development for you, so no machine learning experience is required. You simply need to supply images of objects or scenes you want to identify, and the service handles the rest.


Key features:

Labels

With Amazon Rekognition, you can identify thousands of objects (such as bike, telephone, building), and scenes (such as parking lot, beach, city). When analyzing video, you can also identify specific activities such as "delivering a package" or "playing soccer”.
Custom labels

With Amazon Rekognition Custom Labels, you can extend the detection capabilities of Amazon Rekognition to extract information from images that is uniquely helpful to your business. For example, you can find your corporate logo in social media, identify your products on store shelves, classify your machine parts in an assembly line, or detect your animated characters in videos.
Content moderation

Amazon Rekognition helps you identify potentially unsafe or inappropriate content across both image and video assets and provides you with detailed labels that allow you to accurately control what you want to allow based on your needs.
Text detection

In photos, text appears very differently than neat words on a printed page. Amazon Rekognition can read skewed and distorted text to capture information like store names, street signs, and text on product packaging.
Face detection and analysis
With Amazon Rekognition, you can easily detect when faces appear in images and videos and get attributes such as gender, age range, eyes open, glasses, facial hair for each. In video, you can also measure how these face attributes change over time, such as constructing a timeline of the emotions expressed by an actor.
Face search and verification
Amazon Rekognition provides fast and accurate face search, allowing you to identify a person in a photo or video using your private repository of face images. You can also verify identity by analyzing a face image against images you have stored for comparison.
Celebrity recognition

You can quickly identify well known people in your video and image libraries to catalog footage and photos for marketing, advertising, and media industry use cases.
Pathing
You can capture the path of people in the scene when using Amazon Rekognition with video files. For example, you can use the movement of athletes during a game to identify plays for post-game analysis. 

What are the most common use cases for Amazon Rekognition?

The most common use-cases for Rekognition Image include:

* Searchable Image Library
* Face-Based User Verification
* Sentiment Analysis
* Facial Recognition
* Image Moderation
The most common use-cases for Rekognition Video include:
* Search Index for video archives
* Easy filtering of video for explicit and suggestive content

How can I ensure that Amazon Rekognition meets accuracy goals for my unsafe image or video detection use case?

Amazon Rekognition’s Unsafe Content Detection models have been and tuned and tested extensively, but we recommend that you measure the accuracy on your own data sets to gauge performance.
You can use the ‘MinConfidence’ parameter in your API requests to balance detection of content (recall) vs the accuracy of detection (precision). If you reduce ‘MinConfidence’, you are likely to detect most of the inappropriate content, but are also likely to pick up content that is not actually explicit or suggestive. If you increase ‘MinConfidence’ you are likely to ensure that all your detected content is actually explicit or suggestive but some inappropriate content may not be tagged. For examples on how to use ‘MinConfidence’ for images, please refer to the documentation here.

What face attributes can I get from Amazon Rekognition?

Amazon Rekognition returns the following facial attributes for each face detected, along with a bounding box and confidence score for each attribute:
* Gender
* Smile
* Emotions
* Eyeglasses
* Sunglasses
* Eyes open
* Mouth open
* Mustache
* Beard
* Pose
* Quality
* Face landmarks

What is Amazon Rekognition Video?

Amazon Rekognition Video is a deep learning powered video analysis service that detects activities; understands the movement of people in frame; and recognizes people, objects, celebrities, and inappropriate content from your video stored in Amazon S3. Results are paired with time stamps so that you can easily create an index to facilitate highly detailed video search. For people and faces, Rekognition Video also returns the bounding box coordinates, which is the specific location of the person or face in the frame.
Amazon Rekognition Video can also monitor a live stream that you create from Amazon Kinesis Video Steams to detect and recognize faces from face data that you provide. 

How can I analyze videos in real time?  

In streaming mode, you can search faces against a collection with tens of millions of faces in real time. Rekognition Video face detection and face recognition APIs natively integrate with video stream from Amazon Kinesis Video Streams, a service that enables developers to transmit thousands of live feeds and associated metadata. For security applications, this makes real-time identification of Persons of Interest easy and accurate. 

What is Amazon Rekognition Image?

Rekognition Image is a deep learning powered image recognition service that detects objects, scenes, and faces; extracts text; recognizes celebrities; and identifies inappropriate content in images. It also allows you to search and compare faces. Rekognition Image is based on the same proven, highly scalable, deep learning technology developed by Amazon’s computer vision scientists to analyze billions of images daily for Prime Photos. The service returns a confidence score for everything it identifies so that you can make informed decisions about how you want to use the results. In addition, all detected faces are returned with bounding box coordinates, which is a rectangular frame that fully encompasses the face that can be used to locate the position of the face in the image.

How do I control user access for Amazon Rekognition?

Amazon Rekognition is integrated with AWS Identity and Access Management (IAM). AWS IAM policies can be used to ensure that only authorized users have access to Amazon Rekognition APIs. For more details, please see the Amazon Rekognition Authentication and Access Control page.




