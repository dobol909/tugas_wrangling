def feature_engineering(df):
    df.rename(columns={"dateCreated": "ad_created",
                          "dateCrawled": "date_crawled",
                          "fuelType": "fuel_type",
                          "lastSeen": "last_seen",
                          "monthOfRegistration": "registration_month",
                          "notRepairedDamage": "unrepaired_damage",
                          "nrOfPictures": "num_of_pictures" ,
                          "offerType": "offer_type",
                          "postalCode": "postal_code",
                          "powerPS": "power_ps",
                          "vehicleType": "vehicle_type",
                          "yearOfRegistration": "registration_year"},inplace=True)
    
    #REMOVE $ and , IN PRICE
    df['price'] = df['price'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',',''))
    
    #REMOVE km and , in odometer
    df['odometer'] = df['odometer'].apply(lambda x: x.replace(',','')).apply(lambda x: x.replace('km',''))
    
    #GANTI TIPE DATA
    df = df.astype({'price':'int64','odometer':'int64'})
    
    #Untuk kolom yang bertipe string lakukan pengecekan jumlah data uniknya. Jika perbandingan data unik terlalu besar maka drop kolom tersebut
    #Untuk kolom numeric, drop kolom yang tidak berisi informasi apapun (hanya berisi angka 0)
    #Drop kolom yang informasinya unik disetiap baris datanya ("name") dan kolom yang memiliki banyak kategori namun tidak balance("postal_code")  
    
    df.drop(columns=['name','postal_code','num_of_pictures'],inplace=True)
    
    #REMOVING OUTLIER
    df = df[(df['price'] >= 500) & (df['price'] <= 40000)]
    
    #fillna object dengan modus
    kolum_string = [col for col in df if df[col].dtype == object]
    for i in kolum_string:
        df[i].fillna(df[i].mode(),inplace = True)
    
    #fillna nummerik dengan median
    kolum_nomer = [col for col in df if df[col].dtype == 'int64' or df[col].dtype == 'float64']
    for i in kolum_nomer:
        df[i].fillna(df[i].median,inplace = True)
        
    
    #normalized numerik kolom
    columns_tobe_normalize = ['registration_year','power_ps','odometer','registration_month']
    df[columns_tobe_normalize] = normalize(X=df.loc[:,columns_tobe_normalize], norm="l2", axis=1)
    
    #drop data tipe tanggal
    df.drop(columns=['date_crawled','ad_created','last_seen'],inplace=True)
    
    df_transformed = df
    return df_transformed
    
        