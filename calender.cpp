/*
// prints the entire calender
// of any month or year
*/
#include <iostream>

using namespace std;
void printMonth(int month, int year);
void printYear (int year);
void monthName (int month);
int  monthLen  (int month, int year);
int  leapYear  (int year);
int  weekDay   (int month, int year);

int main(){
	char type;
	int month, year;
	cout<<"Print 'm' for month calender\n";
	cout<<"Print 'y' for  year calender\n";
	cin>>type;
	
	//----ask for month and year input----
	if (type=='m'){
		cout<<"Print month and year: ";
		cin>>month >> year;
		printMonth(month,year);//print a month 
	}		
	else if (type=='y'){
		cout<<"Print year: ";
		cin>>year;
		printYear(year);//print a year 
	}		
	else
		cout<<"Must enter m or y";
	//------------------------------------
	return 0;
}
void printMonth(int month, int year){
	int len = monthLen(month, year);	
	
	//print month name from input 
	monthName(month);cout<< ", "<< year << endl;		
		
	//day layout:
	cout<<"S  M  Tu W  Th F  S\n";
	
	//spaces before the first day 
	int s=weekDay(month, year);
	int j=s+1;
	for(int k=0; k<s; k++){
		cout<<"   ";
	}
	//---------------------------
	
	//loop to print each date of the month with the correct spacing 
	for (int i=1; i<=len; i++){
		if (i<10){
			cout<<i<<"  ";
		}
		else{
			cout<<i<<" ";
		}		
		j++;
		if (j>7){
			cout<<endl;
			j=1;
		}
	}
	cout<<endl<<endl;
	
}

//prints the full year 
//using the printMonth function for each month 
void printYear(int year){
	cout<<"print "<<year<<endl;
	//run it for all 12 months 
	for (int m=1; m<=12; m++){
		printMonth(m,year);
	}
}

//month names with index 
void monthName(int month){
	if (month==1)
		cout<<"JANUARY";
	else if (month==2)
		cout<<"FEBRUARY";
	else if (month==3)
		cout<<"MARCH";
	else if (month==4)
		cout<<"APRIL";
	else if (month==5)
		cout<<"MAY";
	else if (month==6)
		cout<<"JUNE";
	else if (month==7)
		cout<<"JULY";
	else if (month==8)
		cout<<"AUGUST";
	else if (month==9)
		cout<<"SEPTEMBER";
	else if (month==10)
		cout<<"OCTOBER";
	else if (month==11)
		cout<<"NOVEMBER";
	else if (month==12)
		cout<<"DECEMBER";
	else
		cout<<"Invalid month";
	
}

//month length 
int  monthLen(int month, int year){
	//all month lengths with cases:
	int len;
	//(1||3||5||7||8||10||12)=31
	//(4||6||9||11)=30
	if ((month == 1)||
		(month == 3)||
		(month == 5)||
		(month == 7)||
		(month == 8)||
		(month == 10)||
		(month == 12)){
			return len=31;
		}
	else if ((month == 4)||
			 (month == 6)||
			 (month == 9)||
			 (month == 11)){
				return len=30;
			 }
	else if (month == 2) //case for leapyear 
		return len=leapYear(year);
	else
		cout<<"Invalid month";
		return 0;		
}

//determines length of the month february 
int leapYear(int year){
	if (year % 400 == 0 || 
       (year % 4 == 0 && year % 100 != 0)) 
            return (29); 
    else
        return (28);
}


int weekDay(int month, int year){
	//always return the first day of the month 
	//using the gregorian formula 
	int day =1;
	static int t[] = {0, 3, 2, 5, 0, 3, 
					  5, 1, 4, 6, 2, 4};
	year -= month <3;
	int start = (year + year/4 - year/100 + year/400  
				 + t[month-1] + day) % 7;
	return start;			 
}