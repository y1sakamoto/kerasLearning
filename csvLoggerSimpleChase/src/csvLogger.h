//
//  csvLogger.h
//  simpleChase
//
//  Created by YouichiSakamoto on 2018/06/07.
//
//

#ifndef csvLogger_h
#define csvLogger_h


//
//  mouseLogger.h
//  mouseCsvLogger
//
//  Created by YouichiSakamoto on 2018/05/28.
//
//

#ifndef mouseLogger_h
#define mouseLogger_h

#define LOG_SIZE 50
#define LOG_RECORD_SEC 10
#define LOG_START_FRAME 100


#define RECORD_START 1
#define RECORD_STOP 0



class csvLogger{
public:
    csvLogger(){
        
        recording=RECORD_STOP;
        filename="MyRecordedMouseData.csv";
        
    };
    
    void setFileName(const string _filename){
        filename=_filename;
        
    }
    
    
    
    
    
    const bool getLogStart(){
        if(ofGetFrameNum()<LOG_START_FRAME)return false;
        else return true;
    }
    
    
    void startRecord(){
        recording=RECORD_START;
        cout<<"start recording"<<endl;
        
    };
    void stopRecord(){
        recording=RECORD_STOP;
        cout<<"stop recording & clear memorr"<<endl;
        
    };
    
    void setData(const int _x,const int _y){
        if(recording)setToRecord(_x, _y);
    }
    
    void setData(vector <float> &arr){
        if(recording)setToRecord(arr);
    };
    
 
    
    
    
    void clearRecord(){
        csvRecorder.clear();
    };
    void saveData(){
        for(int i=0;i<csvRecorder.size();i++)cout<<csvRecorder[i];
        cout<<endl;
        // Save the recorded values in the csvRecorder ofxCsv object.
        csvRecorder.save("MyRecordedMouseData.csv");
        ofLog() << "Saved " << csvRecorder.getNumRows() << " rows of mouse data";
        cout<<"seve"<<endl;
        
    };
    
    string getStatus(){
        string s;
        if(recording)s+="now recordig \n";
        else s+= "clear&stop recordig \n";
        
        s+= "num rows : ";
        s+=  ofToString(csvRecorder.getNumRows());

        return s;
    };
    
    

private:
    
    
    
    vector<ofVec2f> log;
    ofxCsv csv;
    ofxCsv csvRecorder;
    string filename;
    bool recordingMouse;
    bool recording;
    
    
    void setToRecord(const float _x,const float _y){
        ofxCsvRow row;
        row.setFloat(0, _x);
        row.setFloat(1, _y);
        csvRecorder.addRow(row);
        
    };
    
    void setToRecord(vector <float> &arr){
        if(arr.empty())return;
        ofxCsvRow row;
        for(int i=0;i<arr.size();i++)row.setFloat(i, arr[i]);
        csvRecorder.addRow(row);
        
    };
    
};


#endif /* mouseLogger_h */



#endif /* csvLogger_h */
