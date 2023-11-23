import mlflow

def sum(x,y):
    return x+y
    

if __name__=="__main__":
    # start the server
    with mlflow.start_run():  
        #assign values to x an y       
        x,y=5,10   
                      
        z=sum(x,y)
        
        # Logging /Tracking the experiment with mlflow.
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_metric("z",z)
    
