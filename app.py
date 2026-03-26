import streamlit as st
st.title("Voting App")
st.subheader("Welcome To App")
col1,col2=st.columns(2)
with col1:
    st.text_input("enter name:")
with col2:
    st.text_input("enter last name:")
st.text_input("enter email/gmail")
age=st.number_input("Age",step=1)
aadhar=st.text_input("enter aadhar number: ")
if aadhar.isdigit() and len(aadhar)==12:
    st.write("**success**")
else:
    st.write("Enter Valid Aadhar")
number=st.number_input("enter mobile number: ",min_value=0,step=1, format="%d")  
if len(str(number))==10: 
     st.write("**success**")
else:
    st.write("Enter Valid Mobile Number")  

nums=st.selectbox("your prefernce :",["car","lotus","cup","hand","ring","ele"])
st.write(f"your preference:{nums}")
file=st.file_uploader("Image of thumb:",type=["jpg","jpeg","png"])
if file is not None:
    st.image(file,"uploaded")
else:
    st.write("**File not Found**")
#video=st.video(r"C:\Users\Akshya\OneDrive - Malla Reddy Engineering College for Women\Pictures\Camera Roll\WIN_20260325_12_19_34_Pro.mp4")
st.checkbox("Vote confirmation")
st.button("submit")

