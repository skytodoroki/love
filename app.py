import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

def main():
    st.title("Love Heart with Streamlit")

    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = heart_shape(t)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)

if __name__ == "__main__":
    main()
