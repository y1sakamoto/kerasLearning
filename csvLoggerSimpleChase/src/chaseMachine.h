//
//  chaser.h
//  simpleChase
//
//  Created by YouichiSakamoto on 2018/06/07.
//
//

#ifndef chaser_h
#define chaser_h
class chaseMachine{
public:
    chaseMachine(){
        pos.set(0,0);
        target.set(0,0);
        accel.set(0,0);
    };
    ~chaseMachine(){};
    void setTarget(const ofVec2f _target){target=_target;};
    void update(){

        accel=target-pos;
        accel*=0.02;
        speed+=accel;
        speed*=0.9;
        pos+=speed;
    };
    void draw(){ofDrawCircle(pos, 20);};
    const ofVec2f getPos(){return pos;};
    
private:
    ofVec2f pos;
    ofVec2f speed;
    ofVec2f accel;
    ofVec2f target;

};



#endif /* chaser_h */
