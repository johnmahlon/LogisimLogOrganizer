//
//  main.cpp
//  LogOrganizer
//
//  Created by John Peden on 9/30/15.
//  Copyright © 2015 John Peden. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int main(int argc, const char * argv[]) {
    
    /* Variables */
    ifstream myIn;                  // In file stream
    ofstream myOut;                 // Out file stream
    string line;                    // Stores each line as read
    string header;                  // Stores the header line
    string filename;                // Stores filename
    string oFilename;               // Stores filename for new file
    list<string> linesOfFile;       // List of lines that hold the binary logs
    list<string>::iterator it;      // Itrator for the list
    
    
    
    cout << "Please enter filename: ";          // Prompt for filename
    cin >> filename;                            // Read in filename
    myIn.open(filename.c_str());                // Open filename into filestream
    
    getline(myIn, header);                      // Get the first line of file (header)
    
    it = linesOfFile.begin();                   // Set the iterator
    
    /* Puts the items into the List */
    while (myIn) {
        getline(myIn, line);
        linesOfFile.insert(it, line);
        ++it;
    }
    
    myIn.close();                               // Close input fstream
    
    linesOfFile.sort();                         // Sorts the list
    linesOfFile.unique();                       // Deletes any duplicates
    
    cout << "Enter filename for new file: ";
    cin >> oFilename;
    myOut.open(oFilename);
    
    myOut << header << endl;
    for (it = linesOfFile.begin(); it != linesOfFile.end(); ++it) {
        myOut << *it << endl;
    }
    
    myOut.close();
    
    // Prints list to terminal for debug
    
    /*
    for (it = linesOfFile.begin(); it != linesOfFile.end(); ++it) {
        cout << " " << *it << " " << endl;
    }
    */
    return 0;
}
