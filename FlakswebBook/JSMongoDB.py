

Items = new Mongo.Collection("log_info")

if (Metero.isServer) {
        Meteor.publish('items', function(queryString){
            return query(Items, queryString)
            })
        }



if (Meteor.isClient) {
        Session.set('queryString', '')
        Meteor.subscribe('items', '')

        Template.body.events({
            'keyup #search-box':_.throttle(funciton(event){
                Session.set('queryString', event.target.value)
                Meteor.subscrib('items', event.target.value)
                }, 50)
            })
        }


Template.body.helpers({
    items:funciton(){
        return query(Items, Session.get('queryString'))
        }
    });


