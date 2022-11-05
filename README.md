# FSorter
A quick image sorter with option to take input of labelled data, It can even search in sub folders for image files and sorts images by creating sub directory, images are copied in a directory named Sorted with sub directories as faceID's.

![alt text](https://github.com/[Pranav0-0Aggarwal]/[FSorter]/blob/[main]/APP.png?raw=true)

## Usage
The Program is completely GUI based so no problem should be faced with the usage.
Just Downlaod the master folder and run GUI.py after running PreReq.sh script using the following command

### For Linux/mac users


### For windows users


## Known issues
* Slow
* GUI Freezes after clicking next

## Credits
[ageitguy](https://github.com/ageitgey/face_recognition) for face_recognition module


## Issues because of face_recognition library
* The face recognition model is trained on adults and does not work very well on children. It tends to mix
  up children quite easy using the default comparison threshold of 0.6.
* Accuracy may vary between ethnic groups. Please see [this wiki page](https://github.com/ageitgey/face_recognition/wiki/Face-Recognition-Accuracy-Problems#question-face-recognition-works-well-with-european-individuals-but-overall-accuracy-is-lower-with-asian-individuals) for more details.

## Special Thanks
[Greatwhitehat](https://github.com/greatwhitehat/faceoff) for his faceoff sorter for a basic idea
