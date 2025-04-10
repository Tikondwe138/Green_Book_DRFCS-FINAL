"""Initial migration

Revision ID: 1df35e6a4b6a
Revises: 
Create Date: 2025-03-24 00:43:43.788054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1df35e6a4b6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('disaster',
    sa.Column('disaster_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('severity', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('date_occurred', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('disaster_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('department', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('beneficiary',
    sa.Column('beneficiary_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('impact_score', sa.Integer(), nullable=True),
    sa.Column('nationalid', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.Column('verification_date', sa.DateTime(), nullable=True),
    sa.Column('disaster_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['disaster_id'], ['disaster.disaster_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('beneficiary_id'),
    sa.UniqueConstraint('nationalid'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('chat_log',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=500), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('gis_map',
    sa.Column('map_id', sa.Integer(), nullable=False),
    sa.Column('disaster_id', sa.Integer(), nullable=False),
    sa.Column('coordinates', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['disaster_id'], ['disaster.disaster_id'], ),
    sa.PrimaryKeyConstraint('map_id')
    )
    op.create_table('reports',
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.Column('disaster_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('generated_at', sa.DateTime(), nullable=True),
    sa.Column('format_type', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['disaster_id'], ['disaster.disaster_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('report_id')
    )
    op.create_table('aid_request',
    sa.Column('request_id', sa.Integer(), nullable=False),
    sa.Column('beneficiary_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['beneficiary_id'], ['beneficiary.beneficiary_id'], ),
    sa.PrimaryKeyConstraint('request_id')
    )
    op.create_table('fund',
    sa.Column('fund_id', sa.Integer(), nullable=False),
    sa.Column('donor_name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('allocated_to', sa.Integer(), nullable=True),
    sa.Column('date_received', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['allocated_to'], ['admin.admin_id'], ),
    sa.PrimaryKeyConstraint('fund_id')
    )
    op.create_table('verification_log',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('beneficiary_id', sa.Integer(), nullable=False),
    sa.Column('verified_by', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('remarks', sa.String(length=255), nullable=True),
    sa.Column('verification_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['beneficiary_id'], ['beneficiary.beneficiary_id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('verification_log')
    op.drop_table('fund')
    op.drop_table('aid_request')
    op.drop_table('reports')
    op.drop_table('gis_map')
    op.drop_table('chat_log')
    op.drop_table('beneficiary')
    op.drop_table('admin')
    op.drop_table('users')
    op.drop_table('disaster')
    # ### end Alembic commands ###
