Snapshots = new Mongo.Collection('snapshots');

Snapshots.allow({
	insert: function(userId, doc) {
		return !!userId;
	}
});

Founders = new SimpleSchema({
	name: {
		type: String
	},
});

Metrics = new SimpleSchema({
	name: {
		type: String,
		autoform: {
			afFieldInput: {
				type: 'autocomplete-input',
				placeholder: 'text here',
				settings: function() {
					return {
						position: "bottom",
						limit: 5,
						rules: [{
							collection: Snapshots,
							field: "autocomplete",
							template: Template.userPill
						}, ]
					};
				}
			}
		}
	},
	value: {
		type: String
	}
});

SnapshotSchema = new SimpleSchema({
	CompanyName: {
		type: String,
		label: "Name"
	},
	DataDate: {
		type: String,
		label: "Date"
	},
	Founders: {
		type: [Founders]
	},
	Metrics: {
		type: [Metrics]
	},
	author: {
		type: String,
		label: "Author",
		autoValue: function() {
			return this.userId
		},
		autoform: {
			type: "hidden"
		}
	},
	createdAt: {
		type: Date,
		label: "Created At",
		autoValue: function() {
			return new Date()
		},
		autoform: {
			type: "hidden"
		}
	}
});

Snapshots.attachSchema(SnapshotSchema);