#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    log.setFileName("MyRecordedMouseData.csv");

    //ofxSubscribeOsc(2010, "/predict/", predictPosArry);
    //ofxPublishOsc("localhost", 9001, "/pos/", pos);
    ofSetFrameRate(30);
    recordList.resize(DATASIZE);


}

//--------------------------------------------------------------
void ofApp::update(){
    chaser.update();
    float h=ofGetHeight();
    float w=ofGetWidth();

    recordList[0]=mouseX/w;
    recordList[1]=mouseY/h;
    recordList[2]=chaser.getPos().x/w;
    recordList[3]=chaser.getPos().y/h;

    log.setData(recordList);
    

}

//--------------------------------------------------------------
void ofApp::draw(){
    chaser.draw();
    
    
    string displyStr;
    displyStr+="'s' startRecord \n";
    displyStr+="'r' saveData \n";
    displyStr+="'x' stopRecord + clearRecord \n";
    displyStr+=log.getStatus();

    ofDrawBitmapString(displyStr, 50, 50);
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if(key == 's') {
        log.startRecord();
    }
    if(key == 'r') {
        log.saveData();
    }
    else if(key == 'x') {
        log.stopRecord();
        log.clearRecord();
    }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    const ofVec2f p(x,y);
    chaser.setTarget(p);
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
