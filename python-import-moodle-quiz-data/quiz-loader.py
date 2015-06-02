'''
Created on Feb 8, 2015

@author: hugo
'''
import sys,os, datetime
import logging
import csv
import codecs
from lxml import etree

from os import listdir
from os.path import isfile, join

# for encoding pictures
import base64

def createMap(d):
    # create xml element map from dict
    #type="multichoice"
    
    # read pictures from dir if exists
    picturePath = './pictures'
    pictureFileList = [ f for f in listdir(picturePath) if isfile(join(picturePath,f)) ]

    # top level map element
    mp = etree.Element('question')
    mp.set('type', d['type'])
    
    # add name
    pls = etree.SubElement(mp, 'name')
    txt = etree.SubElement(pls, 'text')
    txt.text = d['question']

    # search for picture to add to question if picture name starts with question id
    qId = d['question'][:3]
    print qId
    
    matchingPictureUri = [p for p in pictureFileList if qId in p]
    
    # does this question have a picture?
    hasPicture = False 
    
    if matchingPictureUri :
        hasPicture = True
        # set path to picture
        uriPicture = './pictures/' + matchingPictureUri[0] 
        # load file and encode in XML base64
        with open(uriPicture, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        
    #questiontext
    qxt = etree.SubElement(mp, 'questiontext')
    qxt.set('format',"html")
    txt = etree.SubElement(qxt, 'text')
    # temp doc to store text to be put in CDATA block
    cdatxt = etree.Element('cdat')

    txtP = etree.SubElement(cdatxt, 'p')
    txtP.text = d['questiontext']
    
    # add picture if exist for question
    if hasPicture:
        # add code to question teext
        #<img src="@@PLUGINFILE@@/blaadjes-aan-boom.jpg" alt="blaadjes aan beslisboom" width="242" height="217" style="vertical-align:text-bottom; margin: 0 .5em;" class="img-responsive">
        imgP = etree.SubElement(cdatxt, 'p')
    
        img = etree.SubElement(imgP, 'img')
        img.set('src',"@@PLUGINFILE@@/"+matchingPictureUri[0])
        img.set('alt',matchingPictureUri[0].split('.')[0])
        img.set('width',"250")
        img.set('height',"250")
        img.set('style',"vertical-align:text-bottom; margin: 0 .5em;")
        img.set('class',"img-responsive")
        
        
        # add picture
        qPictElem = etree.SubElement(qxt, 'file')
        qPictElem.set('name',matchingPictureUri[0])
        qPictElem.set('path',"/")
        qPictElem.set('encoding',"base64")
        qPictElem.text = encoded_string 
        #<file name="blaadjes-aan-boom.jpg" path="/" encoding="base64">
    
    # wrap in CDATA block etree.CDATA(
    strTxt = etree.tostring(cdatxt)
    txt.text = etree.CDATA(strTxt)
    
    #question defaults
    gfb = etree.SubElement(mp, 'generalfeedback')
    gfb.set('format',"html")
    txt = etree.SubElement(gfb, 'text')
    txt.text = ""
    tmp = etree.fromstring('<defaultgrade>1.0000000</defaultgrade>')
    mp.append(tmp)
    tmp = etree.fromstring('<penalty>0.3333333</penalty>')
    mp.append(tmp)
    tmp = etree.fromstring('<hidden>0</hidden>')
    mp.append(tmp)
    tmp = etree.fromstring('<single>false</single>')
    mp.append(tmp)
    tmp = etree.fromstring('<shuffleanswers>true</shuffleanswers>')
    mp.append(tmp)
    tmp = etree.fromstring('<answernumbering>abc</answernumbering>')
    mp.append(tmp)
    tmp = etree.fromstring("""<correctfeedback format="html">
      <text>Your answer is correct.</text>
    </correctfeedback>""")
    mp.append(tmp)
    tmp = etree.fromstring("""<partiallycorrectfeedback format="html">
      <text>Your answer is partially correct.</text>
    </partiallycorrectfeedback>""")
    mp.append(tmp)
    tmp = etree.fromstring("""<incorrectfeedback format="html">
      <text>Your answer is incorrect.</text>
    </incorrectfeedback>""")
    mp.append(tmp)
    tmp = etree.fromstring('<shownumcorrect/>')
    mp.append(tmp)
    
    # if answer is filled then create answer
    if d.has_key('AA') :
        if (d['PA']==""):
            answer = '0'
        else:
            answer = d['PA']
        tmp = etree.fromstring('<answer fraction="'+ answer +'" format="html"><text>' + d['AA'] + """</text>
<feedback format="html">
<text></text>
</feedback>
</answer>""")
        mp.append(tmp)                

    # if answer is filled then create answer
    if d.has_key('AB') :
        if (d['PB']==""):
            answer = '0'
        else:
            answer = d['PB']
        tmp = etree.fromstring('<answer fraction="'+ answer +'" format="html"><text>' + d['AB'] + """</text>
<feedback format="html">
<text></text>
</feedback>
</answer>""")
        mp.append(tmp)                

    # if answer is filled then create answer
    if d.has_key('AC') :
        if (d['PC']==""):
            answer = '0'
        else:
            answer = d['PC']
        tmp = etree.fromstring('<answer fraction="'+ answer +'" format="html"><text>' + d['AC'] + """</text>
<feedback format="html">
<text></text>
</feedback>
</answer>""")
        mp.append(tmp)                

    # if answer is filled then create answer
    if d.has_key('AD') :
        if (d['PD']==""):
            answer = '0'
        else:
            answer = d['PD']
        tmp = etree.fromstring('<answer fraction="'+ answer +'" format="html"><text>' + d['AD'] + """</text>
<feedback format="html">
<text></text>
</feedback>
</answer>""")
        mp.append(tmp)                

    # if answer is filled then create answer
    if d.has_key('AE') :
        if (d['PE']==""):
            answer = '0'
        else:
            answer = d['PE']
        tmp = etree.fromstring('<answer fraction="'+ answer +'" format="html"><text>' + d['AE'] + """</text>
<feedback format="html">
<text></text>
</feedback>
</answer>""")
        mp.append(tmp)                

    # if answer is filled then create answer
    if d.has_key('AF') :
        if (d['PF']==""):
            answer = '0'
        else:
            answer = d['PF']
        tmp = etree.fromstring('<answer fraction="'+ answer +'" format="html"><text>' + d['AF'] + """</text>
<feedback format="html">
<text></text>
</feedback>
</answer>""")
        mp.append(tmp)                

                    
    # return map
    return mp

if __name__ == '__main__':
    # use absolute path for cron job
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # set up logging
    log_file = os.path.join(ROOT_DIR, 'loader.log')
    FORMAT = "%(asctime)s|%(levelname)s|%(message)s"
    logging.basicConfig(filename = log_file, format=FORMAT, filemode='w', level=logging.INFO)
    
    if len(sys.argv) != 2:
        print "Usage: quiz-loader.py <path to input file>\n"
        sys.exit(2)
        
    pref_path = sys.argv[1]
    if os.path.isfile(pref_path):
        print "Reading input file " + pref_path
        logging.info('Reading input file ...')
    
        in_file = codecs.open(pref_path, mode ='rb')
        #prefs = json.load(pref_file)
    else:
        print "Input file not found. exiting\n";
        logging.error('Input file not found, exit ...')   
        sys.exit(2)
        
    # set up xml document
    logging.info('Start reading questions.')
    # get date
    generated_on = str(datetime.datetime.now())

    # top level element
    doc = etree.Element('quiz')
    #doc.set('version', '0.1')
    #doc.set('xmlns',"http://www.dikw.com/moodle/quiz")
    
    # meta data elements
    md = etree.SubElement(doc, 'meta-data')
    comment = etree.Comment('Generated by DIKW for Moodle quiz')
    md.append(comment)
    dc = etree.SubElement(md, 'dateCreated')
    dc.text = generated_on
    
    # row seperator
    sep = '\t'
    
    # read file
    datareader = csv.reader(in_file, delimiter = sep, quotechar='"')
#    datareader = unicode_csv_reader(in_file, delimiter = sep)
    
    firstline = True
    
    logging.info('Start processing input file.')
    
    for line in datareader:
        # load header
        if firstline:
            header = line
            firstline = False
            if len(line) == 1:
                print 'Seems inputfile %s does not use %s as a seperator? Exiting...' % (pref_path,sep)
                logging.error('Wrong seperator?  Stop ...')
                sys.exit()
        else:            
            #line = [x.decode('cp1252') for x in line]
            # make dict object
            d = dict(zip(header, line))
            
            # create mapping element
            # line = line.decode('cp1252')
#            try:
            mp = createMap(d)
#            except:
#                 d['questiontext']
#                 logging.error('Failed on line : '+ str(line) )
            # append comment before each question
            qc = etree.Comment(' question : '+ d['question'])
            doc.append(qc)
            # append mapping to root doc
            doc.append(mp)
    # log
    logging.info('Transformation succesfull.')
        
    # write doc to file
    fname = pref_path.split('.')[0] + '.xml'
    f = open(fname, 'w')
    # oldf.write(etree.tostring(doc, 'utf-8'))
    logging.info('Write to file.')
    
    try:
        #tostring(doc, 'utf-8')
        f.write(etree.tostring(doc, encoding='UTF-8', pretty_print=True))
        f.close()
    except:
        logging.error('Failed to write xml object to file.')
    
    logging.info('Done!')
    
    print 'Done!'
