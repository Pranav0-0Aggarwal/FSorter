import face_recognition as fr
import os
import shutil
import concurrent.futures
from pathlib import Path
import numpy as np

file_ext = ('.jpg', '.png', '.gif', '.jpeg')

class Persons:
    def process(self, file):
        message_3a = f'Processing {file}'
        try:
            image = fr.load_image_file(file)
            face_locations = fr.face_locations(image, number_of_times_to_upsample=0, model='cnn')
            face_encodings = fr.face_encodings(image, face_locations)
            print(f'Processed {file}...')
            return file, face_encodings
    
        except Exception as err:
            message4 = 'ERROR: %s' % err

    img_files = []
    
    def __init__(self, address):
        self.address = os.path.abspath(address)
        if not os.path.isdir(self.address):
            message1 = "ERROR: Source directory must exist"
        if not any(filename.endswith(file_ext) for filename in os.listdir(self.address)):
            message2 = 'ERROR: source directory must contain image files'


    def run(self):
        p = []
        r = []
        for file in os.listdir(self.address):
            if file.endswith(file_ext):
                self.img_files.append(os.path.join(self.address, file))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            message5 = "Running Jobs...."
            results = executor.map(self.process, self.img_files)
            for file,result in results:
                p.append(result)
                name = Path(file).stem
                r.append(name)
        return p,r

class Img:
    img_files = []
    face_counter=0

    def process(self, file):
        message_3a = f'Processing {file}'

        try:
            image = fr.load_image_file(file)
            face_locations = fr.face_locations(image, number_of_times_to_upsample=0, model='cnn')
            face_encodings = fr.face_encodings(image, face_locations)
            print(f'Processed {file}...')
            return file, face_encodings
    
        except Exception as err:
            message4 = 'ERROR: %s' % err


    def __init__(self, address):
        self.address = os.path.abspath(address)
        if not os.path.isdir(self.address):
            message6 = "ERROR: Source directory must exist"
        if not any(filename.endswith(file_ext) for filename in os.listdir(self.address)):
            message7 = 'ERROR: source directory must contain image files'


    def run(self, address, p, r,conditiong):
        s=[]
        s=p
        tolerance=0.6

        parent_dir = address
        self.target = os.path.join(parent_dir, "Sorted")
        if not os.path.exists(self.target):
            os.mkdir(self.target)

        ignore_list=[self.target]
        if len(os.listdir(self.address)) !=0:
            for root, directories, files in os.walk(self.address):
                if root in ignore_list:
                    directories[:] = []
                    files[:] = []
                for file in files:
                    if file.endswith(file_ext):
                        self.img_files.append(os.path.join(root, file))
        else:
            for file in os.listdir(self.address):
                if file.endswith(file_ext):
                    self.img_files.append(os.path.join(self.address, file))

        with concurrent.futures.ProcessPoolExecutor() as executor:
            message8 = 'Running jobs...'
            results = executor.map(self.process, self.img_files)

        for file, face_encodings in results:
            if len(face_encodings) == 0 :
                if not os.path.exists(os.path.join(self.target, 'no_face_found')):
                    os.mkdir(os.path.join(self.target, 'no_face_found'))
                    shutil.copyfile(file, os.path.join(self.target, 'no_face_found', os.path.basename(file)))
            elif conditiong:
                for i in range(0,len(face_encodings)):
                    condition=False
                    for k in range(0,len(s)):
                        boolp=  np.linalg.norm(s[k]-face_encodings[i])
                        match= boolp<=tolerance
                        if match.any():
                            match_index = k
                            face_id = r[k]
                            condition= True
                    if not condition:
                        self.face_counter += 1
                        face_id = 'face%d' % self.face_counter
                    if not os.path.exists(os.path.join(self.target, face_id)):
                        os.mkdir(os.path.join(self.target, face_id)) 
                    s.append(face_encodings[i])
                    r.append(face_id)
                    pathf=os.path.join(self.target, face_id, os.path.basename(file))
                    if not os.path.exists(pathf):
                        shutil.copyfile(file, pathf)
            else:
                    self.face_counter += 1
                    face_id = 'face%d' % self.face_counter
                    if not os.path.exists(os.path.join(self.target, face_id)):
                        os.mkdir(os.path.join(self.target, face_id)) 
                    s.append(face_encodings[i])
                    r.append(face_id)
                    pathf=os.path.join(self.target, face_id, os.path.basename(file))
                    if not os.path.exists(pathf):
                        shutil.copyfile(file, pathf)               



def swag(source,label,conditiong):
    persons = Persons(label)
    p,r = persons.run()
    img = Img(source)
    img.run(source, p, r,conditiong)
    print("GoodBye- Task completed")
