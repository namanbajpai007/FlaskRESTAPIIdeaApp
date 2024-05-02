from flask import Flask, request

app = Flask(__name__)

#Create the Idea repository where ideas will be stored
ideas = {
    1: {
        "id" : 1,
        "idea_name" : "ONDC",
        "idea_description" : "Details about ONDC",
        "idea_author" : "Naman"
    },
    2: {
        "id" : 2,
        "idea_name" : "Save Soil",
        "idea_description" : "Details about Saving Soil",
        "idea_author" : "Shubham"
    }
}

'''
Create a RESTful endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas") #API GET Call & URI
def get_all_ideas():    #CONTROLLER 
    #Logic to fetch all the ideas 
    return ideas 


'''
Create a RESTful endpoint for creating a new idea
'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    try:
        request_body = request.get_json()  # Added parentheses to get_json()
        
        # Check if "id" key is present in the request body
        if "id" not in request_body:
            return "id is missing", 400

        # Check if the idea id passed is not already present
        if request_body["id"] in ideas:
            return "idea with the same id is already present", 404
    
        ideas[request_body["id"]] = request_body
    
        return "idea created and saved successfully", 201
    except:
        return "Some internal server error", 500


'''
End point to fetch idea based on idea id 
'''
@app.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "Idea id passed is not present",400

    except:
        return "Some internal error happened",500


'''
End point to update idea based on idea id 
'''
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json()
            return ideas[int(idea_id)],200 
        else:
            return "Idea id passed is not present",400
        
    except:
        return "Some internal error happened",500


'''
End point to delete an idea 
'''
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id)) #Delete the entry from the Ideas dictionary
            return "Idea got successfully removed"
        else:
            return "Idea id passed is not present",400
        
    except:
        return "Some internal error happened",500


if __name__ == '__main__':
    app.run(port=8080)

