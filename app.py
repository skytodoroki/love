import streamlit as st
import turtle

def draw_heart():
    t = turtle.Turtle()
    t.speed(0)
    t.color('red')
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.hideturtle()

def main():
    st.title("Draw Heart with Turtle")

    col1, col2 = st.beta_columns(2)
    with col1:
        st.image('heart.png')

    with col2:
        st.write("Click the button to draw a heart!")
        if st.button("Draw"):
            draw_heart()

if __name__ == "__main__":
    main()
