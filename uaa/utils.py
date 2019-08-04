import random
import string


# ------------------------------------
# application id generate function
# ------------------------------------
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_application_id_generator(instance):
    new_application_id = random_string_generator().upper()

    klass = instance.__class__
    qs_exists = klass.objects.filter(application_id=new_application_id).exists()
    if qs_exists:
        return unique_application_id_generator(instance)
    return new_application_id
# end of application id gerating function


# ----------------------------------------------
# short name for university model generate
# ----------------------------------------------
def short_name_generator(instance):
	name = instance.name
	name.lower()
	a = name.split()

	for i in a:
		if i=='and' or i=='of' or i=='&':
			a.remove(i)

	new = []
	for i in a:
		new.append(i[0])
	return ''.join(str(x) for x in new)
# end of short name gerating function