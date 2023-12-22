# chat_rules.py

def get_bot_response(user_message):
    user_message = user_message.lower()

    # Define rules for the chatbot
    
    if 'hello' in user_message or 'hi' in user_message or 'hey' in user_message:
        return "Hello there! Welcome to Bensimat Mining Equipment. I'm Bob, your friendly robot assistant. How can I assist you today?"

    elif 'how are you' in user_message:
        return "Thank you for asking! I'm here and ready to help. How can I make your day better?"
    
    elif 'how are you' in user_message:
        return "Thank you for asking! I'm here and ready to help. How can I make your day better?"

    elif 'bye' in user_message:
        return 'Goodbye! If you ever need assistance in the future, don\'t hesitate to reach out. Have a great day!'

    elif 'equipment' in user_message or 'supply' in user_message or 'mining' in user_message:
        return 'Certainly! At Bensimat, we take pride in supplying high-quality mining equipment. What specific information are you looking for?'

    elif 'what' in user_message:
        return 'We offer a variety of mining supplies, including pumps, valves, hoses, PVC pipes, and HDPE pipes. Is there something specific you would like to know more about?'

    elif 'skomota' in user_message and 'know' in user_message:
        return 'Ah, Skomota! A familiar name from my hometown. Feel free to share more, and let\'s chat about it!'

    elif 'what' in user_message and 'services' in user_message or 'service' in user_message:
        return 'Our mining tools cater to all scales of mining, ensuring top-notch quality. How may I assist you further with our services?'
    
    elif 'which' in user_message and 'services' in user_message or 'service' in user_message:
        return 'Our mining tools cater to all scales of mining, ensuring top-notch quality. How may I assist you further with our services?'
    
    elif 'price' in user_message or 'cost' in user_message:
        return 'For pricing information, please contact our sales team at sales@bensimat.com.'

    elif 'order' in user_message or 'buy' in user_message:
        return 'To place an order, please visit our website or contact our sales team at sales@bensimat.com.'

    elif 'contact' in user_message or 'phone' in user_message or 'email' in user_message or 'reach' in user_message or 'get hold' in user_message or 'get a hold' in user_message:
        return 'You can reach us at +1234567890 or via email at info@bensimat.com.'

    elif 'locat' in user_message or 'where' in user_message and 'branches' in user_message :
        return 'We have branches in multiple locations. To find the nearest one, please visit our website or contact us.'

    elif 'recommend' in user_message or 'advice' in user_message:
        return 'Sure, I can help with that! What specific advice or recommendations are you looking for?'
    
    elif 'capabilities' in user_message or 'offer' in user_message:
        return 'Our capabilities include providing state-of-the-art mining equipment, reliable support, and efficient solutions for all your mining needs.'

    elif 'partnership' in user_message or 'collaboration' in user_message:
        return 'We are always open to exploring new partnerships and collaborations. If you have a specific proposal, please contact our business development team.'

    elif 'maintenance' in user_message or 'service' in user_message:
        return 'We offer maintenance services for our supplied equipment. Regular maintenance helps ensure optimal performance and longevity.'

    elif 'sustainability' in user_message or 'environment' in user_message:
        return 'Bensimat is committed to sustainability. We strive to minimize the environmental impact of our operations and promote eco-friendly practices.'
    elif 'capabilities' in user_message or 'offer' in user_message:
        return 'Our capabilities include providing state-of-the-art mining equipment, reliable support, and efficient solutions for all your mining needs.'

    elif 'partnership' in user_message or 'collaboration' in user_message:
        return 'We are always open to exploring new partnerships and collaborations. If you have a specific proposal, please contact our business development team.'

    elif 'maintenance' in user_message or 'service' in user_message:
        return 'We offer maintenance services for our supplied equipment. Regular maintenance helps ensure optimal performance and longevity.'

    elif 'sustainability' in user_message or 'environment' in user_message:
        return 'Bensimat is committed to sustainability. We strive to minimize the environmental impact of our operations and promote eco-friendly practices.'

    elif 'technology' in user_message or 'innovation' in user_message:
        return 'Our commitment to innovation is reflected in the advanced technologies integrated into our mining equipment. We constantly strive to stay at the forefront of industry advancements.'

    elif 'career' in user_message or 'jobs' in user_message:
        return 'If you are interested in joining our team, please visit our Careers page on the website or send your resume to careers@bensimat.com.'

    elif 'events' in user_message or 'conferences' in user_message:
        return 'Stay updated on our latest events and conferences by checking our Events page on the website. We regularly participate in industry events to showcase our products and network with professionals.'

    elif 'blog' in user_message or 'articles' in user_message:
        return 'Explore our Blog section on the website for insightful articles, news, and updates related to the mining industry and our company.'
    
    elif 'blog' in user_message or 'articles' in user_message:
        return 'Explore our Blog section on the website for insightful articles, news, and updates related to the mining industry and our company.'
        # Add more rules based on the needs of your users

    else:
        return "I'm sorry, I didn't quite catch that. Could you please rephrase or provide more details?"