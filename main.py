from flask import Flask, render_template, jsonify, request
import pandas as pd
from data import x_trained_columns
import joblib 



app = Flask(__name__ )
trained_random_forest_model = joblib.load("static/data/trained_rand_forest.joblib")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/prediction')
def predictions():
    return render_template('predictions.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

# #scatter plot routes
@app.route('/Rand_Forest')
def RandForest():
    return render_template('Rand_Forest.html')

@app.route('/Ridge')
def Ridge():
    return render_template('Ridge.html')

@app.route('/LinReg')
def LinReg():
    return render_template('LinReg.html')

@app.route('/Lasso')
def Lasso ():
    return render_template('Lasso.html')

@app.route('/ElastNet')
def ElastNet():
    return render_template('ElastNet.html')
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# def generate_predictions():
#     # prediction = 1
#     # return jsonify([prediction])
    
@app.route('/generate_predictions', methods=['POST'])
def generate_prediction():
    user_inputs=request.json
    predict_df=pd.DataFrame({
    'MSSubClass':[int(user_inputs['MSSubClass'])],
    'MSZoning':[int(user_inputs['MSZoning'])],
    'LotFrontage':[int(user_inputs['LotFrontage'])],
    'LotArea':[int(user_inputs['LotArea'])],
    'Street':[int(user_inputs['Street'])],
    'LotShape':[int(user_inputs['LotShape'])],
    'LandContour':[int(user_inputs['LandContour'])],
    'Utilities':[int(user_inputs['Utilities'])],
    'LotConfig':[float(user_inputs['LotConfig'])],
    'LandSlope':[float(user_inputs['LandSlope'])],
    'Neighborhood':[float(user_inputs['Neighborhood'])],
    'Condition1':[float(user_inputs['Condition1'])],
    'Condition2':[float(user_inputs['Condition2'])],
    'BldgType':[float(user_inputs['BldgType'])],
    'HouseStyle':[float(user_inputs['HouseStyle'])],
    'OverallQual':[float(user_inputs['OverallQual'])],
    'OverallCond':[float(user_inputs['OverallCond'])],
    'YearBuilt':[float(user_inputs['YearBuilt'])],
    'YearRemodAdd':[float(user_inputs['YearRemodAdd'])],
    'RoofStyle':[float(user_inputs['RoofStyle'])],
    'RoofMatl':[float(user_inputs['RoofMatl'])],
    'Exterior1st':[float(user_inputs['Exterior1st'])],
    'Exterior2nd':[float(user_inputs['Exterior2nd'])],
    'MasVnrArea':[float(user_inputs['MasVnrArea'])],
    'ExterQual':[float(user_inputs['ExterQual'])],
    'ExterCond':[float(user_inputs['ExterCond'])],
    'Foundation':[float(user_inputs['Foundation'])],
    'BsmtFinSF1':[float(user_inputs['BsmtFinSF1'])],
    'BsmtFinSF2':[float(user_inputs['BsmtFinSF2'])],
    'BsmtUnfSF':[float(user_inputs['BsmtUnfSF'])],
    'TotalBsmtSF':[float(user_inputs['TotalBsmtSF'])],
    'Heating':[float(user_inputs['Heating'])],
    'HeatingQC':[float(user_inputs['HeatingQC'])],
    'CentralAir':[float(user_inputs['CentralAir'])],
    '1stFlrSF':[float(user_inputs['FirstFlrSF'])],
    '2ndFlrSF':[float(user_inputs['SecondFlrSF'])],
    'LowQualFinSF':[float(user_inputs['LowQualFinSF'])],
    'GrLivArea':[float(user_inputs['GrLivArea'])],
    'BsmtFullBath':[float(user_inputs['BsmtFullBath'])],
    'BsmtHalfBath':[float(user_inputs['BsmtHalfBath'])],
    'FullBath':[float(user_inputs['FullBath'])],
    'HalfBath':[float(user_inputs['HalfBath'])],
    'BedroomAbvGr':[float(user_inputs['BedroomAbvGr'])],
    'KitchenAbvGr':[float(user_inputs['KitchenAbvGr'])],
    'KitchenQual':[float(user_inputs['KitchenQual'])],
    'TotRmsAbvGrd':[float(user_inputs['TotRmsAbvGrd'])],
    'Functional':[float(user_inputs['Functional'])],
    'Fireplaces':[float(user_inputs['Fireplaces'])],
    'GarageYrBlt':[float(user_inputs['GarageYrBlt'])],
    'GarageCars':[float(user_inputs['GarageCars'])],
    'GarageArea':[float(user_inputs['GarageArea'])],
    'PavedDrive':[float(user_inputs['PavedDrive'])],
    'WoodDeckSF':[float(user_inputs['WoodDeckSF'])],
    'OpenPorchSF':[float(user_inputs['OpenPorchSF'])],
    'EnclosedPorch':[float(user_inputs['EnclosedPorch'])],
    '3SsnPorch':[float(user_inputs['ThirdSsnPorch'])],
    'ScreenPorch':[float(user_inputs['ScreenPorch'])],
    'PoolArea':[float(user_inputs['PoolArea'])],
    'MiscVal':[float(user_inputs['MiscVal'])],
    'MoSold':[float(user_inputs['MoSold'])],
    'YrSold':[float(user_inputs['YrSold'])],
    'SaleType':[float(user_inputs['SaleType'])],
    'SaleCondition':[float(user_inputs['SaleCondition'])]

    })
    prediction=str(trained_random_forest_model.predict(predict_df)[0])

    return jsonify([prediction])
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/show_columns')
def show_columns():
    return jsonify(x_trained_columns)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)