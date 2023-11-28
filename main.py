import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout='wide')

st.markdown('# Optimisation of Antenna Design using ML Techniques')
col11, col12 = st.columns(2)
with col11:
    st.subheader('Enabling Simulation Optimised Antenna Design')
    st.markdown('''> Project By: Akshat Punia & Sarvesh Sankaran
                    Under supervision of Prof. Jitendra Prajapti''')

with col12:
    st.image('assets/snioe.png', use_column_width=True)

st.divider()

st.markdown('''
            # Our Abstract
For electromagnetic design problems, various computation methods have been applied and have shown promising results. However, these algorithms often entail **substantial computational expenses** due to the demanding nature of electromagnetic simulations. As a consequence, direct application of these algorithms for optimization can result in extensive time requirements, sometimes spanning weeks. This drawback restricts their applicability within numerous real-world scenarios. This project aims to address this limitation by exploring and implementing machine learning techniques. The objective is to facilitate **simulation- optimized antenna design within a feasible timeframe**. This will be achieved through the utilization of a simulated dataset, encompassing various samples with distinct design parameters while maintaining a consistent substrate material and thickness. The dataset will be generated via the electromagnetic simulator CST Microwave Studio.''')

st.header("Dataset Preparation")
st.write('''

            The essence of the project lies in the creation of a series of designs of Rectangular Mi- crostrip Patch Antenna each optimized for di↵erent frequency ranges simulating their performance and collecting a dataset for machine learning model training. The antennas, ranging from 1 to 10 GHz, are designed using CST Studio, considering various parame- ters such as length, width, and inset length. The goal is to create a dataset that can be leveraged to predict antenna parameters based on frequency and S parameter magnitude.

            Constant Values
            • Height of the Conductor: 0.035 mm • Height of the Substrate: 1.6 mm
            • Width of the Feedline: 3.137 mm
            • Height of Inset: 1mm
            • Material for Ground and Patch: Copper (Annealed)
            • Material for Substrate: FR-4 (Lossy)
         
These constant values provide a foundation for the designs, ensuring uniformity and adhering to industrial norms. The choice of materials, specifically copper for the ground and patch and FR-4 for the substrate, aligns with common industry practices for Mi- crostrip patch antennas.
Simulations in CST Studio yield S parameter results for each antenna design. 

The overarching objective is to develop a machine learning module capable of predict- ing antenna parameters—length, width, and inset length—based on the frequency and magnitude of the S parameters. The dataset is structured to encompass input features such as frequency and magnitude, with corresponding outputs being the antenna parame- ters. The utilization of consistent values across designs provides a controlled environment for the study.

''')
col21, col22 = st.columns(2, gap='small')
with col21:
    with st.expander("4GHz Design"):
        st.image('assets/4inset1.png',width = 250)
        st.image('assets/4inset2.png',width = 250)


with col22:
    with st.expander("8GHz Design"):
        st.image('assets/8inset1.png',width = 250)
        st.image('assets/4inset3.png',width = 250)


with st.expander("Show Dataset"):
    st.write(pd.read_csv("Inset_Dataset.csv"))

col31, col32 = st.columns(2, gap='small')
with col31:
    st.image('assets/s1to2.png', width = 620, caption="S parameters for different parameter values from a single design based on frequency range from 1 to 2 Ghz")
with col32:
    st.image('assets/s4to5.png', width = 620, caption="S parameters for different parameter values from a single design based on frequency range from 4.5 to 5.5 Ghz")

st.header("ML Model Tuning")
with st.expander("Click to see Detailed Steps"):
    st.write('''
                **Dataset Compilation:** The dataset, crucial for the ML model, was compiled from a range of simulations. This data is instrumental in training the machine learning model to predict optimal antenna parameters.
                
            **Model Selection** The RandomForestRegressor was chosen due to its robustness and e↵ectiveness in han- dling regression tasks with high-dimensional data, characteristic of electromagnetic design problems.
            
            **Data Preparation** The dataset was loaded into a pandas DataFrame, a flexible and powerful data manip- ulation tool for Python, allowing for easy data analysis and manipulation. The dataset consists of input features such as the frequency and magnitude of the S parameters, with the target variables being the length (L), width (W), and inset length (b) of the antenna.
                
            **Splitting the Data** A key step in machine learning model preparation is splitting the dataset into training and testing sets. This is crucial for evaluating the model’s performance on unseen data. The standard practice of an 80-20 split provides a substantial amount of data for training while reserving enough for an unbiased assessment of the model’s generalization capabilities.
                
            **Model Training** The RandomForestRegressor model, a collection of decision trees, is known for its high accuracy and ability to run in parallel. It’s an ensemble method that fits multiple decision tree classifiers on various sub-samples of the dataset and averages the results to improve predictive accuracy and control over-fitting.
                
            **Performance Evaluation** Training the model involves adjusting the decision trees to best fit the training data. The Mean Squared Error (MSE) metric is used post-training on the test set to quantify the model’s prediction accuracy.
                
            **Model Evaluation and Visualization**  Visualizations of the actual versus predicted values o↵er an intuitive understanding of the model’s performance. The proximity of the predicted points to the actual points indicates the level of precision achieved by the RandomForestRegressor model.
            ''')
with st.expander("Show Code Snippet"):
    st.code('''
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.metrics import mean_squared_error

            file_path = ’Dataset_inset.xlsx’
            df = pd.read_excel(file_path)

            X_rev = df[[’F’, ’Mag(db)’]]
            y_rev = df[[’L’, ’W’, ’b’]]
            X_rev_train, X_rev_test, y_rev_train, y_rev_test = train_test_split(X_rev, y_rev, test

            model_rev = RandomForestRegressor(n_estimators=100, random_state=42)
            model_rev.fit(X_rev_train, y_rev_train)

            y_rev_pred = model_rev.predict(X_rev_test)

            mse_rev = mean_squared_error(y_rev_test, y_rev_pred)
            print(f’Mean Squared Error for L, W, b: {mse_rev}’)
            ''')

with st.expander("Show Predicted Dataset"):
    st.write(pd.read_csv('Predicted_Parameters.csv'))

st.header("Simulation of Predicted Values")
st.write("S Parameters and releveant metrics for 4 differnt frequencies")
col41, col42 = st.columns(2, gap='small')
with col41:
    with st.expander("1.4GHz Design"):
        st.image('assets/data14.png',use_column_width=True)
        st.image('assets/pred14img.png',use_column_width=True)
        st.image('assets/pred14.png',use_column_width=True)

with col42:
    with st.expander("4.5GHz Design"):
        st.image('assets/data45.png',use_column_width=True)
        st.image('assets/pred45im.png',use_column_width=True)
        st.image('assets/pred45.jpg',use_column_width=True)


st.header("Contribute to the Project")
st.write("Feel free to contribute to the dataset which is openly available on our github repository. We would also appreciate pull requests if you find any part of this project to be in error.")
if st.button("Contribute on GitHub"):
    st.write("Redirecting to GitHub...")
    st.markdown("[Click Here If Redirect does not happen automatically](https://github.com/akshatpunia26/optimal-antenna-design)")

