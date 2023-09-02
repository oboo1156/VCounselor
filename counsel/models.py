from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

Hashtag = (
    ('education', 'educative'),
    ('gossip', 'gossip'),
    ('creating', 'creating'),
    ('hawt', 'hawt'),
    ('sad', 'sad'),
    ('relationship', 'relationship'),
    ('interesting', 'interesting'),
    ('funny', 'funny')

)

Hashtagg = (
    ('education', 'educative'),
    ('gossip', 'gossip'),
    ('creating', 'creating'),
    ('hawt', 'hawt'),
    ('sad', 'sad'),
    ('relationship', 'relationship'),
    ('interesting', 'interesting'),
    ('funny', 'funny')

)

class Counsellor(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='counsellor/%Y/%m/%d', null=True)
    contact = PhoneNumberField(null=True)
    whatsapp = models.URLField(null=True)
    text = models.TextField(null=True) #short description about them
    twitter = models.URLField(null=True)
    meet = models.URLField(null=True)
    website = models.URLField(null=True)
    reviews = models.IntegerField(null=True)
    date = models.DateField(null=True, auto_now_add=True)
    #story = models.TextField(null=True)#counsellors advice to us or story to share. its is part of their details. counsellors
    #college = models.TextField(null=True)
    #will act like they are sharing their story and it will appear as ListView on Advice Link

    # class Meta:
    #     ordering = ('-date', 'college')

    def __str__(self):
        return self.name


class Client(models.Model):
    reaL_name = models.CharField(max_length=200, null=True)
    nick_name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='client/%Y/%m/%d',  null=True)
    time = models.TimeField(null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    story = models.TextField(null=True)#will the story be sorted by date and hashtag, if not create new model for story
    hashtag = models.CharField(choices=Hashtag, max_length=50, null=True)#sort by most recent,hashtag,like story. bring a hashtag
    hashtagg = models.CharField(choices=Hashtagg, max_length=50, null=True)
    #like

    class Meta:
        ordering = ('-date', 'hashtag')

    def __str__(self):
        return self.story #no 'see more'


class Comment(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    #counsellor = models.ForeignKey('Counsellor', on_delete=models.CASCADE, null=True)
    # like replyonescomment at(@)
    date = models.DateTimeField(null=True, auto_now_add=True)
    reply = models.TextField(null=True)

    class Meta:
        ordering = ('-date',)#'like', 'counsellor'

    def __str__(self):
        return self.reply


class CommentReply(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    # like replyonescomment at @
    reply = models.TextField(null=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.reply

#djjango app on post and reply so i know if i should get a db for reply
#sort reply/comments by counsellors and peer counsellors before any other comment. try and make ordering in admin.py by
#counsellor and see ordering = ('counsellor', 'date')


# from django.db import models
# from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField
#
# class Contact(models.Model):
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = PhoneNumberField(validators=[phone_regex], blank=True)

