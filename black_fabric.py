import random
import streamlit as st

random.seed(random.randint(0,9999))

st.header('Black Fabric Name Generator')

st.markdown('Credit to [@yedoye](https://twitter.com/yedoye_/status/1422264318079422466) for the idea and everyone in the replies.')
st.write("Click 'Submit' to get a list of 5 names.")

submit = st.button('Submit')

if submit:

	fabric = ["Nylon", "Cotton", "Polyester", "Silk", "Bunting", "Burlap", "Tweed", "Corduroy", "Canvas", "Cheesecloth", "Chiffon", "Chino", "Chintz", "Denim", "Flannel", "Gingham", "Herringbone", "Kente", "Longcloth", "Moleskin", "Madras", "Muslin", "Satin", "Sateen", "Twill", "Baize", "Fleece", "Velveteen", "Felt", "Wool", "Jersey", "Velour", "Lace", "Gore-Tex", "Spandex", "Windstopper", "Houndstooth", "Paisley", "Angora", "Cashmere", "Hemp", "Jute", "Kevlar", "Linen", "Mohair", "Pashmina", "Leather"]

	surnames = ["Jones", "Collins", "Wilson", "Smith", "McDonald", "Griffiths", "Peters", "Rashford", "Rogers", "Parker", "Williams", "Cooper", "Brown", "Johnson", "Richardson", "Thomas", "Spencer", "Banks", "White", "Black", "Green", "Bell", "Carter", "Carson", "Clark", "Campbell", "Davis", "Griffin", "Cole", "Cook", "Daniels", "Dunlap", "Dunn", "Edwards", "Ewing", "Fisher", "Fox", "Gibbs", "Jackson", "West", "Yancey", "Mitchell", "Moore", "Phillips", "Plumber", "Butcher", "Ross", "Taylor", "Stevens", "Watson", "Wilson", "Jefferson"]

	for n in range(5):

		fabric_names = (random.choice(fabric), random.choice(surnames))

		fn_text = ' '.join(fabric_names)

		st.write(fn_text)