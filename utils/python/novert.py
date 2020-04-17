from .profile import create_readme
from .maj_min import create_minmaj


def classify(ver1, ver2):
    data = dict(ver1, **ver2)
    novices = dict()
    experts = dict()
    for user in data:
        if data[user]['userInfo']['content']['read'] == 'Yes' or \
                data[user]['userInfo']['content']['speak'] == 'Yes'or \
                data[user]['userInfo']['content']['write'] == 'Yes':
            experts.update({user: data[user]})
        else:
            novices.update({user: data[user]})
    return novices, experts


def create_novert(ver1, ver2):
    novices, experts = classify(ver1, ver2)
    create_readme(novices, 'Domain/Novice', 'Analysis of Telugu Novice')
    create_minmaj(novices, 'Domain/Novice')
    create_readme(experts, 'Domain/Expert', 'Analysis of Telugu Experts')
    create_minmaj(experts, 'Domain/Expert')
