Metrics = new Mongo.Collection('metrics');

Metrics.allow({
	insert: function(userId, doc) {
		return !!userId;
	}
});

MetricsSchema = new SimpleSchema({
	CompanyName: {
		type: String,
		label: "Name"
	},
	DataDate: {
		type: Date,
		label: "Date"
	}
});

Metrics.attachSchema(MetricsSchema);