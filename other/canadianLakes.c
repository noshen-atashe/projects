/*
// program for analysing data of canadian lakes
// from the file "data.txt"
*/
  
# include <stdio.h> 
# include <string.h> 
# include <stdlib.h>

//function for calculating max temperature
int maxTemp(double temp[]);
//function for calculating min temperature
int minTemp(double temp[]);
//main   
int main( ) 
{   
    char lake[6][10]={
		"Sup.","Mich.","Huron","Erie","Ont.","St.Clr"
	};
	
	//file pointer 
    FILE *filePointer ;      
    //variable for the data to be read from file 
    int n = 6;
	char dataToBeRead[n];
	//pointer for data string
	char* ptr;  
	//open file "data.txt" for reading
    filePointer = fopen("data.txt", "r") ; 
    
	//variables for storing data
	//and calculating avg
	int i=1;
	int j=1;
	double val;
	double sum[6];
	double avg[6];
	double sumT=0.0;
	double avgT=0.0;
	//initialize all sum and avg to 0
	for(int k=0; k<6; k++){
		sum[k]=0.0;
		avg[k]=0.0;
	}	
	
    //check if file exist 
    if ( filePointer == NULL ){ 
        printf( "data.txt file failed to open." ) ; 
    } 
    else{           
        printf("Reading from data.txt\n"); 
		
        // Read the dataToBeRead from the file 
        while(fgets(dataToBeRead, n, filePointer) != NULL){      
            if(i>2){
				//convert each entry to a double 
				val=strtod(dataToBeRead,&ptr);			
				sum[j-1] += val;
				j++;
			}
			//variable updates
			//for data alignment
			i++;
			if(i>8){
				i=1;
				j=1;
				n=6;				
			}
			if(i==2){
				n=7;
			}else if((i>2)){				
				n=9;
			}		
        }
		// Closing the file using fclose() 
        fclose(filePointer) ;
		printf("\n");
		printf("--------------------------\n");
		printf("Part 1a: Yearly average temperature for each lake\n");	
		for(int k=0; k<6; k++){
			avg[k]=sum[k]/365;
			//printf("sum of lake[%d] = %lf\n",k+1,sum[k]);
			printf("avg of %s = %.2lf\n",lake[k],avg[k]);
		}
		
		printf("\nPart 1b: Yearly average temperature of all lakes combined\n");
		for(int k=0; k<6; k++){
			sumT += avg[k];
		}
		avgT = sumT/6;
		printf("avg of all lakes = %.2lf\n",avgT);
		printf("--------------------------\n");
		printf("Part 2a: Coldest and Warmest avg temperatures\n");
		int max=maxTemp(avg);
		int min=minTemp(avg);
		printf("%s is the warmest lake with avg temperature:%.2lf\n",lake[max],avg[max]);
		printf("%s is the coldest lake with avg temperature:%.2lf\n",lake[min],avg[min]);
		printf("\nPart 2b: Comparison with average temperature\n");
		printf("Lakes with average yearly temperature above the total average\n");
		for(int i=0; i<6; i++){
			if(avg[i]>avgT){
				printf("%s with avg temperate %.2lf\n",lake[i],avg[i]);
			}
		}
		printf("Lakes with average yearly temperature below the total average\n");
		for(int i=0; i<6; i++){
			if(avg[i]<avgT){
				printf("%s with avg temperate %.2lf\n",lake[i],avg[i]);
			}
		}
		printf("--------------------------\n");
		
    } 
    return 0;         
} 
//function for calculating max temperature
int maxTemp(double temp[]){
	int m = temp[0];
	int k = 0;
	for(int i=1;i<6;i++){
		if(temp[i]>m){
			m=temp[i];
			k=i;
		}
	}
	return k;
}
//function for calculating min temperature
int minTemp(double temp[]){
	int m = temp[0];
	int k = 0;
	for(int i=1;i<6;i++){
		if(temp[i]<m){
			m=temp[i];
			k=i;
		}
	}
	return k;
}