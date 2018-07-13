#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

    //ofxSubscribeOsc(2010, "/action/", obs.getAction());
    
    ofxSubscribeOsc(2010, "/action/",
        [=](vector<float> _action) {
            obs.setNumFrame((int)_action[0]);
            obs.updateFromAction(ofVec2f(_action[1],_action[2]));
        
        });
    
    ofxSubscribeOsc(2010, "/reset/", [=](int val) {
        obs.setResetFlag();
    });
    
    //ofxSubscribeOsc(2010, "/reset/",});
    ofxPublishOsc("localhost", 9001, "/observation/", obs.observationArray);
    ofSetFrameRate(30);

    mode=MODE_RECORD;
}

//--------------------------------------------------------------
void ofApp::update(){
    float h=ofGetHeight();
    float w=ofGetWidth();
    ofVec2f m(mouseX,mouseY);
    obs.setPlayerPos(
        ofVec2f(    m.x/ofGetWindowWidth(),
                    m.y/ofGetWindowHeight()));
    obs.update();
}

//--------------------------------------------------------------
void ofApp::draw(){
    Agent.draw(obs);

   

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

    
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    const ofVec2f p(x,y);
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
