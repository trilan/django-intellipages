===================
django-intellipages
===================

This app provides only one tiny template filter for now. It allows you to
output page navigation like this::

    1 ... 6 7 _8_ 9 10 ... 32

(where ``8`` is the current page number).

Usage
=====

Add ``intellipages`` to ``INSTALLED_APPS``. In your templates do::

    {% load intellipages %}
    
    {% for p in page|intellipages %}
        {% if p %}
            {% ifequal p page.number %}
                {{ p }}
            {% else %}
                <a href="?page={{ p }}">{{ p }}</a>
            {% endifequal %}
        {% else %}
            ...
        {% endif %}
    {% endfor %}

(where ``page`` is a ``django.core.paginator.Page`` instance).

Or::

    {% load intellipages %}
    
    {% for p in paginator|intellipages:number %}
        {% if p %}
            {% ifequal p number %}
                {{ p }}
            {% else %}
                <a href="?page={{ p }}">{{ p }}</a>
            {% endifequal %}
        {% else %}
            ...
        {% endif %}
    {% endfor %}

(where ``page`` is a ``django.core.paginator.Paginator`` instance, and
``number`` is a variable of type ``int``).