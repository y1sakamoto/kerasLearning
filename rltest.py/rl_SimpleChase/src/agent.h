//
//  agent.h
//  rl_SimpleChase
//
//  Created by YouichiSakamoto on 2018/06/27.
//
//

#ifndef agent_h
#define agent_h
#define PLAYER_STOP_COUNT_MAX 1000

class agent{
public:
    void setup(){};
    void update(){};
    void updatePlayer(observation &obs,ofVec2f _pos){
        _pos.x/=ofGetWidth();
        _pos.y/=ofGetHeight();
        obs.setPlayerPos(_pos);};
    
    void setAction(observation &obs,ofVec2f _action){
        _action.x*=ofGetWidth();
        _action.y*=ofGetHeight();
        obs.updateFromAction(_action);};
    
    void draw(observation &obs){
        ofDrawBitmapString(obs.getInformation(), 50, 50);
        ofVec2f agentPos=obs.getAgentPos();
        ofVec2f playerPos=obs.getPlayerPos();
        agentPos.x*=ofGetWidth();
        agentPos.y*=ofGetHeight();
        playerPos.x*=ofGetWidth();
        playerPos.y*=ofGetHeight();
        
        ofDrawCircle(playerPos.x,playerPos.y,10);
        ofDrawCircle(agentPos.x,agentPos.y,10);

    };
    
    
    

    
private:
    

    bool getDone(observation &obs){
        if(obs.getPlayerSpeed().length()<0.000001)count();
        else resetCount();
        if(countMax())obs.isDone();
        if(obs.isOutPos())obs.isDone();

    };
    
    
    
    int count(){
        static int counter;
        counter++;
        return counter;
    };
    int resetCount(){
        static int counter;
        counter=0;

        
    }
    
    
    
    bool countMax(){
        static int counter;
        if(counter>PLAYER_STOP_COUNT_MAX)return true;
        else return false;
        
    };


};



#endif /* agent_h */
