FlowRouter.route('/', {
	name: 'home',
	action() {
		BlazeLayout.render('MainLayout', {
			main: 'Snapshots'
		});
	}
});
FlowRouter.route('/viz', {
	name: 'viz',
	action() {
		BlazeLayout.render('VizLayout', {
			main: 'Snapshots'
		});
	}
});