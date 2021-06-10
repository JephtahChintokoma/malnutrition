from flask import Flask, jsonify, request, render_template
from experta import *
app = Flask(__name__) # Flask Instance
# import os

# print(os.getcwd())

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}
# results = dict()
# slight_hair=slight_hair, reddish_hair=reddish_hair, hair_falling=hair_falling, abnormal_skin=abnormal_skin, swollen_face=swollen_face, glazed_eyes=glazed_eyes, apathetic=apathetic, smaller_muscles=smaller_muscles, anaemic=anaemic, diarrhoea=diarrhoea, bloated_stomach=bloated_stomach,older_face=older_face, cranky_child=cranky_child,wrinkled_skin=wrinkled_skin ,little_fattie_tissue=little_fattie_tissue ,converse_stomach_rib_prominent=converse_stomach_rib_prominent ,chronic_infections=chronic_infections, skin_reddish_purging=skin_reddish_purging, age=age


def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		#symptoms=os.path.dirname("symptoms/"+ disease + ".txt")
		disease_s_file = open("Dsymptoms/"+ disease + ".txt") 
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Ddescriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Dtreatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" %(id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details+"\n")
    print("The common treatments recommended by experts are: \n")
    print(treatments+"\n")

    # results.append('guinea')

    self.results["disease"] = f"The most probable disease that you have is {id_disease}"
    self.results["details"] = f"A short description of the disease is given below :\n {disease_details}"
    self.results["treatments"] = f"The common treatments recommended by experts are: \n {treatments}"
    


# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(bloated_stomach, thin_limbs,reddish hair, swollen face):
class Greetings(KnowledgeEngine):

    # global results 
    results = dict()
    # self.run()

    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! I am Dr.Jephtah, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        print("")
        # self.slight_hair=slight_hair
        # self.reddish_hair=reddish_hair
        # self.hair_falling=hair_falling, 
        # self.abnormal_skin=abnormal_skin
        # self.swollen_face=swollen_face
        # self.glazed_eyes=glazed_eyes
        # self.apathetic=apathetic
        # self.smaller_muscles=smaller_muscles
        # self.anaemic=anaemic
        # self.diarrhoea=diarrhoea
        # self.bloated_stomach=bloated_stomach,older_face=older_face
        # self.cranky_child=cranky_child
        # self.wrinkled_skin=wrinkled_skin
        # self.little_fattie_tissue=little_fattie_tissue
        # self.converse_stomach_rib_prominent=converse_stomach_rib_prominent
        # self.chronic_infections=chronic_infections
        # self.skin_reddish_purging=skin_reddish_purging
        # self.age=age

        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(slight_hair=W())),salience = 1)
    def symptom_0(self):
	    self.declare(Fact(slight_hair=slight_hair))

    @Rule(Fact(action='find_disease'), NOT(Fact(reddish_hair=W())),salience = 1)
    def symptom_1(self):
        self.declare(Fact(reddish_hair=reddish_hair))

    @Rule(Fact(action='find_disease'), NOT(Fact(hair_falling=W())),salience = 1)
    def symptom_2(self):
        self.declare(Fact(hair_falling=hair_falling))

    @Rule(Fact(action='find_disease'), NOT(Fact(abnormal_skin=W())),salience = 1)
    def symptom_3(self):
        self.declare(Fact(abnormal_skin=abnormal_skin))

    @Rule(Fact(action='find_disease'), NOT(Fact(swollen_face=W())),salience = 1)
    def symptom_4(self):
        self.declare(Fact(swollen_face=swollen_face))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(glazed_eyes=W())),salience = 1)
    def symptom_5(self):
        self.declare(Fact(glazed_eyes=glazed_eyes))

    @Rule(Fact(action='find_disease'), NOT(Fact(apathetic=W())),salience = 1)
    def symptom_6(self):
        self.declare(Fact(apathetic=apathetic))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(smaller_muscles=W())),salience = 1)
    def symptom_7(self):
        self.declare(Fact(smaller_muscles=smaller_muscles))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(anaemic=W())),salience = 1)
    def symptom_8(self):
        self.declare(Fact(anaemic=anaemic))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(diarrhoea=W())),salience = 1)
    def symptom_9(self):
        self.declare(Fact(diarrhoea=diarrhoea))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(bloated_stomach=W())),salience = 1)
    def symptom_10(self):
        self.declare(Fact(bloated_stomach=bloated_stomach))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(thin_body=W())),salience = 1)
    def symptom_11(self):
        self.declare(Fact(thin_body=thin_body))

    @Rule(Fact(action='find_disease'), NOT(Fact(older_face=W())),salience = 1)
    def symptom_12(self):
        self.declare(Fact(older_face=older_face))

    @Rule(Fact(action='find_disease'), NOT(Fact(cranky_child=W())),salience = 1)
    def symptom_13(self):
        self.declare(Fact(cranky_child=cranky_child))

    @Rule(Fact(action='find_disease'), NOT(Fact(wrinkled_skin=W())),salience = 1)
    def symptom_14(self):
        self.declare(Fact(wrinkled_skin=wrinkled_skin))

    @Rule(Fact(action='find_disease'), NOT(Fact(little_fattie_tissue=W())),salience = 1)
    def symptom_15(self):
        self.declare(Fact(little_fattie_tissue=little_fattie_tissue))

    @Rule(Fact(action='find_disease'), NOT(Fact(converse_stomach_rib_prominent=W())),salience = 1)
    def symptom_16(self):
        self.declare(Fact(converse_stomach_rib_prominent=converse_stomach_rib_prominent))

    @Rule(Fact(action='find_disease'), NOT(Fact(chronic_infections=W())),salience = 1)
    def symptom_17(self):
        self.declare(Fact(chronic_infections=chronic_infections))

    @Rule(Fact(action='find_disease'), NOT(Fact(skin_reddish_purging=W())),salience = 1)
    def symptom_18(self):
        self.declare(Fact(skin_reddish_purging=skin_reddish_purging))

    @Rule(Fact(action='find_disease'), NOT(Fact(age=W())),salience = 20)
    def symptom_19(self):
        self.declare(Fact(age=age))		   


    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="no"),Fact(bloated_stomach="yes"),Fact(thin_body="no"),Fact(older_face="no"),Fact(child_cranky="no"),Fact(wrinkled_skin="no"),Fact(little_fattie_tissue="no"),Fact(converse_stomach_rib_prominent="no"),Fact(chronic_infections="no"),Fact(skin_reddish_purging="no"),Fact(age="no"))
    def disease_0(self):
        self.declare(Fact(disease="Kwashiorkor"))

    @Rule(Fact(action='find_disease'),Fact(slight_hair="no"),Fact(reddish_hair="no"),Fact(hair_falling="no"),Fact(abnormal_skin="yes"),Fact(swollen_face="no"),Fact(glazed_eyes="no"),Fact(apathetic="no"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="no"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="no"))
    def disease_1(self):
        self.declare(Fact(disease="Marasmus"))

    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="yes"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="no"))
    def disease_2(self):
        self.declare(Fact(disease="Marasmus-Kwashiorkor"))	

    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="no"),Fact(bloated_stomach="yes"),Fact(thin_body="no"),Fact(older_face="no"),Fact(child_cranky="no"),Fact(wrinkled_skin="no"),Fact(little_fattie_tissue="no"),Fact(converse_stomach_rib_prominent="no"),Fact(chronic_infections="no"),Fact(skin_reddish_purging="no"),Fact(age="yes"))
    def disease_3(self):
        self.declare(Fact(disease="Kwashiorkor_"))	

    
    @Rule(Fact(action='find_disease'),Fact(slight_hair="no"),Fact(reddish_hair="no"),Fact(hair_falling="no"),Fact(abnormal_skin="yes"),Fact(swollen_face="no"),Fact(glazed_eyes="no"),Fact(apathetic="no"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="no"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="yes"))
    def disease_4(self):
        self.declare(Fact(disease="Marasmus_"))	


    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="yes"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="yes"))
    def disease_5(self):
        self.declare(Fact(disease="Marasmus-Kwashiorkor_"))	
        

    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def disease(self, disease):
        # global res
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" %(id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details+"\n")
        print("The common treatments recommended by experts are: \n")
        print(treatments+"\n")


        self.results["disease"] = f"The most probable disease that you have is {id_disease}"
        self.results["details"] = f"A short description of the disease is given below :\n {disease_details}"
        self.results["treatments"] = f"The common treatments recommended by experts are: \n {treatments}"


    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def if_not_matched(disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" %(id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details+"\n")
        print("The common treatments recommended by experts are: \n")
        print(treatments+"\n")

    # results.append('guinea')

        self.results["disease"] = f"The most probable disease that you have is {id_disease}"
        self.results["details"] = f"A short description of the disease is given below :\n {disease_details}"
        self.results["treatments"] = f"The common treatments recommended by experts are: \n {treatments}"


    @Rule(Fact(action='find_disease'),
        Fact(slight_hair=MATCH.slight_hair),
        Fact(reddish_hair=MATCH.reddish_hair),
        Fact(hair_falling=MATCH.hair_falling),
        Fact(abnormal_skin=MATCH.abnormal_skin),
        Fact(swollen_face=MATCH.swollen_face),
        Fact(glazed_eyes=MATCH.glazed_eyes),
        Fact(apathetic=MATCH.apathetic),
        Fact(smaller_muscles=MATCH.smaller_muscles),
        Fact(anaemic=MATCH.anaemic),
        Fact(diarrhoea=MATCH.diarrhoea),
        Fact(bloated_stomach=MATCH.bloated_stomach),
        Fact(thin_body=MATCH.thin_body),
        Fact(older_face=MATCH.older_face),
        Fact(cranky_child=MATCH.cranky_child),
        Fact(wrinkled_skin=MATCH.wrinkled_skin),
        Fact(little_fattie_tissue=MATCH.little_fattie_tissue),
        Fact(converse_stomach_rib_prominent=MATCH.converse_stomach_rib_prominent),
        Fact(chronic_infections=MATCH.chronic_infections),
        Fact(skin_reddish_purging=MATCH.skin_reddish_purging),
        Fact(age=MATCH.age),NOT(Fact(disease=MATCH.disease)),salience = -999)


    def not_matched(self,slight_hair, reddish_hair, hair_falling, abnormal_skin, swollen_face, glazed_eyes, apathetic, smaller_muscles, anaemic, diarrhoea, bloated_stomach,thin_body,older_face, cranky_child,wrinkled_skin ,little_fattie_tissue ,converse_stomach_rib_prominent ,chronic_infections, skin_reddish_purging, age):
        global max_disease
        print("\nDid not find any disease that matches your exact symptoms")
        self.results['message'] = '\nDid not find any disease that matches your exact symptoms'
        lis = [slight_hair, reddish_hair, hair_falling, abnormal_skin, swollen_face, glazed_eyes, apathetic, smaller_muscles,anaemic ,diarrhoea ,bloated_stomach ,thin_body ,older_face, wrinkled_skin, cranky_child, little_fattie_tissue, converse_stomach_rib_prominent, chronic_infections, skin_reddish_purging, age]
        max_count = 0
        max_disease = ""
        for key,val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0,len(lis)):
                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)
        #    self.diziz = max_disease





engine = Greetings() # Knowledge Engine Instance

@app.route("/", methods=(("GET", "POST")))
def index():
    preprocess()
    global slight_hair, reddish_hair, hair_falling, abnormal_skin, swollen_face, glazed_eyes, apathetic, smaller_muscles, anaemic, diarrhoea, bloated_stomach, thin_body,older_face, cranky_child,wrinkled_skin ,little_fattie_tissue ,converse_stomach_rib_prominent ,chronic_infections, skin_reddish_purging, age
    if request.method == "POST":
        engine.reset()
        slight_hair = request.form.get("slight_hair")
        reddish_hair = request.form.get("reddish_hair")
        hair_falling = request.form.get("hair_falling")
        abnormal_skin = request.form.get("abnormal_skin")
        swollen_face = request.form.get("swollen_face")
        glazed_eyes = request.form.get("glazed_eyes")
        apathetic = request.form.get("apathetic")
        smaller_muscles = request.form.get("small_muscles")
        anaemic =  request.form.get("anaemic")
        diarrhoea = request.form.get("diarrhoea")
        bloated_stomach = request.form.get("bloated_stomach")
        thin_body = request.form.get("thin_body")
        older_face = request.form.get("older_face")
        cranky_child = request.form.get("cranky_child")
        wrinkled_skin = request.form.get("wrinkled_skin")
        little_fattie_tissue = request.form.get("little_fattie_tissue")
        converse_stomach_rib_prominent = request.form.get("converse_stomach_rib_prominent")
        chronic_infections = request.form.get("chronic_infections")
        skin_reddish_purging = request.form.get("skin_reddish_purging")
        age=request.form.get("age")

    # engine.reset()  # Instantiate Initial Fact
        engine.run()

        # Declare Facts
        # engine.declare(Fact(slight_hair=slight_hair))
        # engine.declare(Fact(reddish_hair=reddish_hair))
        # engine.declare(Fact(hair_falling=hair_falling))
        # engine.declare(Fact(abnormal_skin=abnormal_skin))
        # engine.declare(Fact(swollen_face=swollen_face))
        # engine.declare(Fact(glazed_eyes=glazed_eyes))
        # engine.declare(Fact(apathetic=apathetic))
        # engine.declare(Fact(small_muscles=small_muscles))
        # engine.declare(Fact(anaemic=anaemic))
        # engine.declare(Fact(diarrhoea=diarrhoea))
        # engine.declare(Fact(bloated_stomach=bloated_stomach))
        # engine.declare(Fact(thin_body=thin_body))
        # engine.declare(Fact(older_face=older_face))
        # engine.declare(Fact(cranky_child=cranky_child))
        # engine.declare(Fact(wrinkled_skin=wrinkled_skin))
        # engine.declare(Fact(little_fattie_tissue=little_fattie_tissue))
        # engine.declare(Fact(converse_stomach_rib_prominent=converse_stomach_rib_prominent))
        # engine.declare(Fact(chronic_infections=chronic_infections))
        # engine.declare(Fact(skin_reddish_purging=skin_reddish_purging))
        # engine.declare(Fact(age=age))

        # engine.run()

    print(engine.facts)

  
    # return next(i)
    return jsonify(engine.facts)
    
	# jsonify({})


if __name__ == "__main__":
	preprocess()
	app.run(debug=True)		
			
# if __name__ == "__main__":
# 	preprocess()
# 	while(1):
# 		engine.reset()  # Prepare the engine for the execution.
# 		engine.run()  # Run it!
# 	app.run(debug=True)	

