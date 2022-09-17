
from google.cloud import vision_v1 as vision
import io

# Activate Google vision API using service account key
client = vision.ImageAnnotatorClient.from_service_account_json("apikey.json")
image = vision.types.Image()


# Set environment the pictures
def environment():
    import os
    from os import listdir
    from os.path import isfile, join
    
    global path
    path = os.path.join(os.getcwd(),"imgs/")
    
    global pics
    pics = [f for f in listdir(path) if isfile(join(path, f))]
    # pics = ["happy.png","angry.png","happy2.png"]
    
def detect_faces_local():
    global pics
    for pic in pics:
        print("File:", pic)
        pic = path+pic
        
        with io.open(pic, "rb") as image_file:
            parse = image_file.read()
        
        query = {"image": {"content": parse},
                "features": [{"type_": "FACE_DETECTION"}]}
        
        response = client.annotate_image(query)

        # Face expression detection
        faces = response.face_annotations
        likelihood_name = ("UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", "POSSIBLE", "LIKELY", "VERY_LIKELY")
        if faces:
            for index, face in enumerate(faces):
                print("Face", index + 1)
                print("Joy: {}".format(likelihood_name[face.joy_likelihood]))
                print("Sorrow: {}".format(likelihood_name[face.sorrow_likelihood]))
                print("Anger: {}".format(likelihood_name[face.anger_likelihood]))
                print("Surprise: {}".format(likelihood_name[face.surprise_likelihood]))
                vertices = (["({},{})".format(vertex.x, vertex.y)
                            for vertex in face.bounding_poly.vertices])
                print("Face Bounds: {}".format(", ".join(vertices)), end = "\n\n")
                
                
if __name__ == "__main__":
    environment()
    # print(path)
    detect_faces_local()