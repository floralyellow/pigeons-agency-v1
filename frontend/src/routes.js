const routes = [
    {
        'name': 'register',
        'path': '/login',
        'component': Login,
    },
    {
        'name': 'index',
        'path': '/',
        'component': Index,
        'roles': ['ROLE_USER'],
    },
 ];