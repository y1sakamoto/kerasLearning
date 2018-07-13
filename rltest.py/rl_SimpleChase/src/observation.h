//
//  observation.h
//  rl_SimpleChase
//
//  Created by YouichiSakamoto on 2018/06/28.
//
//

#ifndef observation_h
#define observation_h
#define MAX_STOP_COUNT 500
#include "ofMain.h"

class observation{
public:
    observation(){resetData();};
    ~observation(){};
    
    void updateFromAcction(ofVec2f _action){
        setResetDone();
        setAction(_action);
        updateObservation();
        setDone();
        setObservationArray(observationArray);
    }
    

    
    
    
    void setPlayerPos(const ofVec2f _pos){playerPos=_pos;};
    void isDone(){done=true;};

    
    void reset(){
        done=false;
        agentPos.set(0.5,0.5);
        agentPos_past.set(0.5,0.5);
        agentSpeed.set(0,0);
    };

    bool getDone(){return done;};

    const ofVec2f getAgentPos(){return agentPos;};
    const ofVec2f getPlayerPos(){return playerPos;};
    const ofVec2f getPlayerSpeed(){return playerSpeed;};
    
    bool isOutPos(){
        if( playerPos.x<0||playerPos.x>1||
            playerPos.y<0||playerPos.y>1||
            agentPos.x<0||agentPos.x>1||
            agentPos.y<0||agentPos.y>1) return true;
        else return false;

    };

    
    
    
    string getInformation(){
        string s;
        
        s+="frame:"+ofToString(numFrame)+"\n\n";

        s+="playerPos.x:"+ofToString(playerPos.x)+"\n";
        s+="playerPos.y:"+ofToString(playerPos.y)+"\n";
        s+="playerPos_past.x:"+ofToString(playerPos_past.x)+"\n";
        s+="playerPos_past.y:"+ofToString(playerPos_past.y)+"\n";
        s+="playerSpeed.x:"+ofToString(playerSpeed.x)+"\n";
        s+="playerSpeed.y:"+ofToString(playerSpeed.y)+"\n";
        
        s+="playerSpeed_length:"+ofToString(playerSpeed_length)+"\n\n";
        
        s+="agentPos.x:"+ofToString(agentPos.x)+"\n";
        s+="agentPos.y:"+ofToString(agentPos.y)+"\n";
        s+="agentPos_past.x:"+ofToString(agentPos_past.x)+"\n";
        s+="agentPos_past.y:"+ofToString(agentPos_past.y)+"\n";
        s+="agentSpeed.x:"+ofToString(agentSpeed.x)+"\n";
        s+="agentSpeed.y:"+ofToString(agentSpeed.y)+"\n\n";
        
        
        
        s+="diffSpeed.x:"+ofToString(diffSpeed.x)+"\n";
        s+="diffSpeed.y:"+ofToString(diffSpeed.y)+"\n";
        s+="diffPos.x:"+ofToString(diffPos.x)+"\n";
        s+="diffPos.y:"+ofToString(diffPos.y)+"\n";
        s+="distPos:"+ofToString(distPos)+"\n\n";
    
        s+="reward:"+ofToString(reward)+"\n\n";
        
        s+="action.x:"+ofToString(action.x)+"\n";
        s+="action.y:"+ofToString(action.y)+"\n\n";
  
        s+="done:"+ofToString(done)+"\n\n";
        
        return s;
        
        
    };
    
    ofVec2f &getAction(){
        return action;};
    void setNumFrame(int _frame){numFrame=_frame;};
    vector <float>observationArray;

private:
    
    
    
    float reward;
    bool done;
    ofVec2f action;
    
    ofVec2f playerPos;
    ofVec2f playerPos_past;
    
    ofVec2f playerSpeed;
    float playerSpeed_length;
    ofVec2f agentPos;
    ofVec2f agentPos_past;
    
    ofVec2f agentSpeed;
    ofVec2f diffSpeed;
    ofVec2f diffPos;
    float distPos;

    
    int numFrame;

    
    
    void setAction(ofVec2f _action){action=_action;};
    
    void setDone(){
        if(getDoneFromPos()||getDoneFromStopCount())done=true;
        
    }
    
    void setResetDone(){
        if(getResetFromPos()){
            done=false;
            resetData();
        }
      
    }
    
    
    const bool getResetFromPos(){
        bool _b=false;
        if(done==true){
            const float _dist=ofDist((float)ofGetWindowWidth()/2, (float)ofGetWindowHeight()/2,ofGetMouseX(), ofGetMouseY());
            if(_dist<200)_b=true;
        }

        //cout<<_dist<<endl;
        return _b;
    
        
    }
    
    
    
    const bool getDoneFromPos(){
        bool _b=false;
        if( playerPos.x<0||playerPos.x>1||
           playerPos.y<0||playerPos.y>1||
           agentPos.x<0||agentPos.x>1||
           agentPos.y<0||agentPos.y>1){
            _b=true;
        }
        return _b;
        
        
    }
    
    
    const bool getDoneFromStopCount(){
        bool _b=false;
        static int _stopCount;
        if(playerSpeed_length==0)_stopCount++;
        else _stopCount=0;
        if(_stopCount>MAX_STOP_COUNT)_b=true;
        
        return _b;
        
    }
    
    void updateObservation(){
        playerSpeed=playerPos-playerPos_past;
        playerPos_past=playerPos;
        playerSpeed_length=playerSpeed.length();
        agentSpeed=agentPos-agentPos_past;
        agentPos_past=agentPos;
        
        diffSpeed=playerSpeed-agentSpeed;
        diffPos=playerPos-agentPos;
        
        distPos=ofDist(playerPos.x,playerPos.y,agentPos.x,agentPos.y);
        
        agentPos+=action;
        reward+=playerSpeed_length;
        
    };
    
    void setObservationArray(vector <float>&arr){
        arr.clear();
        arr.shrink_to_fit();
        arr.push_back(numFrame);

        arr.push_back(playerPos.x);
        arr.push_back(playerPos.y);
        arr.push_back(playerPos_past.x);
        arr.push_back(playerPos_past.y);
        arr.push_back(playerSpeed.x);
        arr.push_back(playerSpeed.y);
        arr.push_back(playerSpeed_length);
        
        arr.push_back(agentPos.x);
        arr.push_back(agentPos.y);
        arr.push_back(agentPos_past.x);
        arr.push_back(agentPos_past.y);
        arr.push_back(agentSpeed.x);
        arr.push_back(agentSpeed.y);
        
        arr.push_back(diffSpeed.x);
        arr.push_back(diffSpeed.y);
        arr.push_back(diffPos.x);
        arr.push_back(diffPos.y);
        arr.push_back(distPos);
    }
    
    void resetData(){
        
        reward=0;
        action.set(0,0);
        playerPos_past=playerPos;
        
        playerSpeed.set(0,0);
        playerSpeed_length=0;
        agentPos.set(0.5,0.5);
        agentPos_past=agentPos;
        
        agentSpeed.set(0,0);
        diffSpeed.set(0,0);
        diffPos.set(0,0);
        distPos=0;
        
        
    }
    
};


#endif /* observation_h */
