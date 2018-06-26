from mongoengine import Document, fields


class DirectCampaignReport(Document):
    campaign_id = fields.LongField(required=True)
    campaign_name = fields.StringField(required=True)
    date = fields.DateTimeField()
    clicks = fields.LongField()
    total_cost = fields.FloatField()
    type_name = fields.StringField()


class MetrikaSourceSummaryReport(Document):
    source_id = fields.LongField(required=True)
    date = fields.DateTimeField()
    rid = fields.StringField()
    name = fields.StringField()
    group_id = fields.StringField()
    group_name = fields.StringField()
    visits = fields.LongField()
    users_count = fields.LongField()
    bounce_rate = fields.FloatField()
    page_depth = fields.FloatField()
    avg_visit_duration = fields.FloatField()
