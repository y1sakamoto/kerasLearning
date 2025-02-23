#pragma once

#include "ofMain.h"
#include "ofxCsv.h"
#include "ofxOscPublisher.h"
#include "ofxOscSubscriber.h"
#define MODE_RECORD 0
#define MODE_PLAY 1


#define DATASIZE 4


#include "observation.h"
#include "agent.h"

class ofApp : public ofBaseApp{

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);
        vector<float> recordList;
        string displyStr;
        bool mode;
        observation obs;
        agent Agent;
    int val;
};
