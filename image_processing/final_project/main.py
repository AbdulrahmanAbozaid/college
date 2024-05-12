"""Attendence management System"""
from models.datastore import storage
from models.encoder import Encoder
from datetime import datetime
from tkinter import *
from tkinter import ttk, filedialog
import csv
from models.utils import get_attendence
from datetime import datetime, date
from tkinter import *
import face_recognition as fr
from models.datastore import attendence
from models.utils import get_id


class HandleBoard:
	"""Handle Window"""

	@staticmethod
	def get_past():
		try:
			dt = date.today()
			with open(f'{dt}.csv', newline='') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					attendence[row['ID']] = row['Time']
		except FileNotFoundError:
			pass

	@staticmethod
	def get_img_faces_dialog():
		"""get img path"""
		file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
		if not file_path:
			return

		image = fr.load_image_file(file_path)
		face_encodings = fr.face_encodings(image)
		for face_encoding in face_encodings:
			success, sid = get_id(face_encoding)
			print(success, sid)
			if not success:
				continue
			now = datetime.now().strftime('%H:%M:%S')
			print(sid)
			attendence[f"{sid}"] = now
			# setattr(attendence, f"{sid}", now)

		HandleBoard.writeData()

	@staticmethod
	def writeData():
		tree.delete(*tree.get_children())
		dt = date.today()
		with open(f'{dt}.csv', 'w', newline='') as csvfile:
			fieldnames = ['ID', 'Time']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for k, v in get_attendence().items():
				writer.writerow({'ID': k, 'Time': v})
				tree.insert('', 'end', values=(k, v))
		# HandleBoard.update_table()

	@staticmethod
	def update_table():
		tree.delete(*tree.get_children())
		print(get_attendence())
		for k, v in get_attendence().items():
			tree.insert('', 'end', values=(k, v))


if __name__ == '__main__':
	HandleBoard.get_past()
	# Encoder.store_encodes("experiments/testingfast")
	encodes = Encoder.get_encodes()
	if len(encodes) == 0:
			Encoder.store_encodes("experiments/testingfast")
			encodes = Encoder.get_encodes()
	print(len(encodes))

	# GUI

	window = Tk()
	window.title("Face Recognition System")

	# Buttons for GUI
	upload_button = Button(window, text="Choose Image", command=HandleBoard.get_img_faces_dialog, bg="blue", fg="white")
	upload_button.grid(row=0, column=0, padx=10, pady=10)  # Placed above the table

	# Display table for detected users
	tree = ttk.Treeview(window, columns=('ID', 'Time'), show='headings')
	tree.heading('ID', text='ID')
	tree.heading('Time', text='Time')
	tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')  # Positioned below the button

	# Initialize table with existing data
	HandleBoard.update_table()

	window.mainloop()
	storage.save()