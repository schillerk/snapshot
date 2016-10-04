Meteor.publish('recipes', function() {
	return Recipes.find();
});

Meteor.publish('metrics', function() {
	return Metrics.find();
});