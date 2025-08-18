from flask import Flask, render_template, redirect, request, flash
from flask_mysqldb import MySQL
from datetime import datetime
from email.mime.text import MIMEText

app = Flask(__name__, template_folder="templates")
app.secret_key = "a_very_secret_and_random_string"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'gain_infinity_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/case')
def case():
    return render_template('case.html')

@app.route('/case-details')
def case_details():
    return render_template('case-details.html')


@app.route('/blog')
def blog():
    cur = mysql.connection.cursor()

    # Get comment counts for each post
    cur.execute("""
        SELECT post_id, COUNT(*) as comment_count
        FROM comments
        GROUP BY post_id
    """)
    comment_data = cur.fetchall()
    cur.close()

    # Convert to dictionary for easy lookup: { post_id: count }
    comment_counts = {row['post_id']: row['comment_count'] for row in comment_data}

    # Pass the comment counts to the template
    return render_template('blog.html', comment_counts=comment_counts)


@app.route('/marketing-strategies')
def marketing_strategies():
    post_id = 1
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('marketing-strategies.html', post_id=post_id, comments=comments)

@app.route('/branding-starts-with-the-people-close-to-you')
def branding_starts_with_the_people_close_to_you():
    post_id = 2
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('branding-starts-with-the-people-close-to-you.html', post_id=post_id, comments=comments)

@app.route('/reasons-why-your-business-needs-a-website.html')
def reasons_why_your_business_needs_a_website():
    post_id = 3
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('reasons-why-your-business-needs-a-website.html', post_id=post_id, comments=comments)

@app.route('/branding-is-not-just-logo-design')
def branding_is_not_just_logo_design():
    post_id = 4
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('branding-is-not-just-logo-design.html', post_id=post_id, comments=comments)

@app.route('/keyword-to-improve-seo-and-traffic')
def keyword_to_improve_seo_and_traffic():
    post_id = 5
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('keyword-to-improve-seo-and-traffic.html', post_id=post_id, comments=comments)

@app.route('/influence-of-branding-on-customers')
def influence_of_branding_on_customers():
    post_id = 6
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('influence-of-branding-on-customers.html', post_id=post_id, comments=comments)

@app.route('/basic-requirements-for-business-branding')
def basic_requirements_for_business_branding():
    post_id = 7
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('basic-requirements-for-business-branding.html', post_id=post_id, comments=comments)

@app.route('/importance-of-business-branding')
def importance_of_business_branding():
    post_id = 8
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments WHERE post_id = %s ORDER BY created_at DESC", (post_id,))
    comments = cur.fetchall()
    cur.close()
    return render_template('importance-of-business-branding.html', post_id=post_id, comments=comments)   

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

@app.route('/seo')
def seo():
    return render_template('seo.html')    

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/service-details')
def service_details():
    return render_template('service-details.html')



# @app.route("/send_whatsapp", methods=["POST"])
# def send_whatsapp():
#     first_name = request.form.get('first_name')
#     last_name = request.form.get('last_name')
#     email = request.form.get('email')
#     subject = request.form.get('subject')
#     message = request.form.get('message')

#     text = f"Name: {first_name} {last_name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
#     encoded_text = urllib.parse.quote(text)
#     phone_number = "2347047350000"
#     return redirect(f"https://wa.me/{phone_number}?text={encoded_text}")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # if request.method == "POST":
    #     first_name = request.form.get("first_name")
    #     last_name = request.form.get("last_name")
    #     email = request.form.get("email")
    #     subject = request.form.get("subject")
    #     message = request.form.get("message")

    #     full_message = f"""
    #     Name: {first_name} {last_name}
    #     Email: {email}
    #     Subject: {subject}
    #     Message: {message}
    #     """

    #     try:
    #         sender_email = "prosperityadedayo@gmail.com"
    #         sender_password = "wmitlevxbtjftwze"  # Google App Password
    #         receiver_email = "prosperityadedayo@gmail.com"

    #         msg = MIMEText(full_message)
    #         msg["Subject"] = subject
    #         msg["From"] = sender_email
    #         msg["To"] = receiver_email

    #         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #             server.login(sender_email, sender_password)
    #             server.sendmail(sender_email, receiver_email, msg.as_string())

    #         flash("Message sent successfully!", "success")
    #     except Exception as e:
    #         flash(f"Failed to send message: {e}", "error")

    return render_template("contact.html")

# @app.route('/add_comment', methods=['POST'])
# def add_comment():
#     name = request.form.get('name')
#     comment = request.form.get('comment')
#     post_slug = request.form.get('post_slug')
#     timestamp = datetime.now()

#     if not name or not comment or not post_slug:
#         return jsonify({"status": "error", "message": "Missing fields"}), 400

#     cur = mysql.connection.cursor()
#     cur.execute(
#         "INSERT INTO comments (name, comment, post_slug, timestamp) VALUES (%s, %s, %s, %s)",
#         (name, comment, post_slug, timestamp)
#     )
#     mysql.connection.commit()
#     cur.close()

#     return jsonify({
#         "status": "success",
#         "name": name,
#         "comment": comment,
#         "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S')
#     })
@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('name')
    email = request.form.get('email')
    comment_text = request.form.get('comment')
    post_id = request.form.get('post_id')

    if not name or not email or not comment_text:
        flash("All fields are required", "error")
        return redirect(request.referrer)

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO comments (post_id, name, email, comment)
        VALUES (%s, %s, %s, %s)
    """, (post_id, name, email, comment_text))
    mysql.connection.commit()
    cur.close()

    flash("Comment added successfully!", "success")
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug=True)