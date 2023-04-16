# Mage_Hackathon_2023
Mage Hackathon Spring 2023 Submission for BobaTeaHee

## Datasets
The project started by finding some datasets that had user information, website performance information and purchase information. The following datasets were found on Kaggle: 

User_Churn_Dataset
https://www.kaggle.com/datasets/fridrichmrtn/user-churn-dataset

User_Data
https://www.kaggle.com/datasets/sandragracenelson/user-data

The User_Churn_Dataset had ~49k entries whereas the User_Data only had ~400 entries. Since this is a sample use case, the decision was made to augment the User_Data by randomly repeating rows. 

## Pipeline Planning
Once the datasets had been found, some different categories of traits were established.
1. The gender of the visitors would help establish a client demographic. 
2. The number of sessions would provide insights on customer retention. 
3. The number of website interactions that the user had (clicking buttons etc.) would indicate how smooth or rough the user exerience is. 
4. Whether or not someone purchased something would indicate how successful the company is at selling their product. 

## Results
![MAGE](https://user-images.githubusercontent.com/87444586/232321954-4d2283b3-5f9f-4dda-9143-2a3adce23c4a.jpg)
The initial layout was created in a drawing to create a high level plan. 


![MageTree](https://user-images.githubusercontent.com/87444586/232321920-d773ea36-dcc3-4761-9ebb-10db00e65631.png)
The final tree from the MAGE product.

![MageAgeStats](https://user-images.githubusercontent.com/87444586/232322476-96cac32a-8100-4456-8573-1d994caa2842.png)
The most common age demographic appears to be middle age. 


![MageGenderStats](https://user-images.githubusercontent.com/87444586/232321905-6b451568-f30a-46c2-86d5-9275b8f43e7c.png)
This histogram clearly shows that the number of men/women that shop at this store are approximately equal. The User_Data was transformed from female/male to 0 and 1. 

![MagePurchaseStats](https://user-images.githubusercontent.com/87444586/232321911-f0c44e20-d4b4-43f0-9bd6-efb2c08a9e4c.png)
It seems like only about 40% of the people that come to this website actually purchase something. 

![MageSessionInteractions](https://user-images.githubusercontent.com/87444586/232321914-a3d5bd03-2085-4d5b-b896-fa1a18a7a171.png)
The majority of people that come to this site only press 2 buttons. This could either mean that they don't spend much time on the site, or it means that they are able to accomplish everything they need to with 2 interactions.
