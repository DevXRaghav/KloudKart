from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Simulating dynamic pricing data (in a real scenario, you could fetch this from an external API)
cloud_platforms = [
    {
        'name': 'AWS',
        'plans': [
            {'name': 'Basic', 'price': '$10/month', 'storage': '50GB', 'features': 'Compute, Storage, Networking'},
            {'name': 'Pro', 'price': '$30/month', 'storage': '150GB', 'features': 'Compute, Storage, Networking, Security'},
            {'name': 'Enterprise', 'price': '$100/month', 'storage': '500GB', 'features': 'Compute, Storage, Networking, Security, AI'}
        ]
    },
    {
        'name': 'Azure',
        'plans': [
            {'name': 'Basic', 'price': '$12/month', 'storage': '60GB', 'features': 'Compute, Storage, Networking'},
            {'name': 'Standard', 'price': '$40/month', 'storage': '200GB', 'features': 'Compute, Storage, Networking, Security'},
            {'name': 'Premium', 'price': '$120/month', 'storage': '600GB', 'features': 'Compute, Storage, Networking, Security, AI, Big Data'}
        ]
    },
    {
        'name': 'Google Cloud',
        'plans': [
            {'name': 'Basic', 'price': '$8/month', 'storage': '40GB', 'features': 'Compute, Storage, Networking'},
            {'name': 'Advanced', 'price': '$35/month', 'storage': '170GB', 'features': 'Compute, Storage, Networking, Security'},
            {'name': 'Business', 'price': '$110/month', 'storage': '550GB', 'features': 'Compute, Storage, Networking, Security, AI, Machine Learning'}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', cloud_platforms=cloud_platforms)

@app.route('/compare', methods=['POST'])
def compare():
    selected_plans = request.form.getlist('plans')
    
    if not selected_plans:
        return redirect(url_for('index'))

    comparison_result = []
    for platform in cloud_platforms:
        platform_plans = []
        for plan in platform['plans']:
            if plan['name'] in selected_plans:
                platform_plans.append(plan)
        if platform_plans:
            comparison_result.append({'platform': platform['name'], 'plans': platform_plans})

    return render_template('result.html', comparison_result=comparison_result)

if __name__ == '__main__':
    app.run(debug=True)
