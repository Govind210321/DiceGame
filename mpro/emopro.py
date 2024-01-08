import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model
import av
import webbrowser
import base64
import streamlit as st

model  = load_model(r"C:\Users\govin\OneDrive\Documents\Desktop\chanti project\model.h5") 
#model  = load_model(r"F:\Downloads\Moodify-main\Moodify-main\model.h5")
label = np.load(r"C:\Users\govin\OneDrive\Documents\Desktop\chanti project\labels.npy") 
#label = np.load(r"F:\Downloads\Moodify-main\Moodify-main\labels.npy")
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils


class EmotionProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		##############################
		frm = cv2.flip(frm, 1)

		res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

		lst = []

		if res.face_landmarks:
			for i in res.face_landmarks.landmark:
				lst.append(i.x - res.face_landmarks.landmark[1].x)
				lst.append(i.y - res.face_landmarks.landmark[1].y)

			if res.left_hand_landmarks:
				for i in res.left_hand_landmarks.landmark:
					lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
					lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			if res.right_hand_landmarks:
				for i in res.right_hand_landmarks.landmark:
					lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
					lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			lst = np.array(lst).reshape(1,-1)

			pred = label[np.argmax(model.predict(lst))]

			print(pred)
			cv2.putText(frm, pred, (50,50),cv2.FONT_ITALIC, 1, (255,0,0),2)

			if pred!='':
				np.save(r"C:\Users\govin\OneDrive\Documents\Desktop\chanti project\emotion.npy", np.array([pred]))
				#np.save(r"F:\Downloads\mpro (1)\mpro\emotion.npy", np.array([pred]))
				#st.session_state["emotion"]=pred
			#print(st.session_state["emotion"])

		#drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_TESSELATION,
		#						landmark_drawing_spec=drawing.DrawingSpec(color=(0,0,255), thickness=-1, circle_radius=1)) #,
								#connection_drawing_spec=drawing.DrawingSpec(thickness=1))
		#drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
		#drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)


		##############################

		return av.VideoFrame.from_ndarray(frm, format="bgr24")

