Meteor.publish('snapshots', function() {
	return Recipes.find();
});