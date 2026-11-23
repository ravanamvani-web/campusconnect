@app.route('/')
def index():
    try:
        response = supabase.table('users').select("*").execute()
    except APIError as error:
        return f'<p>Error loading users: {error.message}</p>'

    users = response.data

    html = '<h1>users</h1><ul>'
    for user in users:
        html += f'<li>{user["name"]}</li>'
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run(debug=True)